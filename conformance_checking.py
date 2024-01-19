import pm4py
import pandas as pd
import csv
import numpy as np
from datetime import datetime


# def is_abnormal(event_log, net, im, fm, threshold):
#     # 判断是否异常的函数
#     fitness = pm4py.fitness_alignments(event_log, net, im, fm)['averageFitness']
#     return fitness >= threshold


# file_path = 'data/bpic12.csv'
# event_log = pm4py.format_dataframe(pd.read_csv(file_path), case_id='Case ID', activity_key='Activity', timestamp_key='ws')
# net, im, fm = pm4py.read_pnml('process_model/ilp_0.5.pnml')

# 读取过程模型
net, im, fm = pm4py.read_pnml('data/normal_heuristics.pnml')

# # 对事件日志进行一致性检查
# file_path = 'data/abnormal_patient.csv'
# event_log = pm4py.format_dataframe(pd.read_csv(file_path), case_id='c', activity_key='e', timestamp_key='t')
# F = pm4py.fitness_token_based_replay(event_log, net, im, fm)
# fitness = pm4py.fitness_token_based_replay(event_log, net, im, fm)['average_trace_fitness']
# precision = pm4py.precision_token_based_replay(event_log, net, im, fm)
# f1score = 2 * fitness * precision / (fitness + precision)
# print('fitness:' + str(fitness))
# print('precision:' + str(precision))
# print('f1score:' + str(f1score))

# # 读取模拟ground_truth
# ground_truth_path = 'ground_truth.csv'
# ground_truth = pd.read_csv(ground_truth_path).set_index('c')['r'].to_dict()

# 读取ground_truth
ground_truth_path = 'data/gold_standard.csv'
df = pd.read_csv(ground_truth_path)
ground_truth = []
for index, row in df.iterrows():
    ground_truth.append(row['1dAVb'] + row['RBBB'] + row['LBBB'] + row['SB'] + row['AF'] + row['ST'] > 0)

# 读取事件日志并计算适应度
result = dict()
test_file_path = 'data/patient.csv'
df = pd.read_csv(test_file_path)
df = df[df['c'] >= 600]
test_event_log = pm4py.format_dataframe(df, case_id='c', activity_key='e', timestamp_key='t')
dfs = [group for _, group in test_event_log.groupby('c')]   # 拆成trace
for df in dfs:
    case_id = df['c'].iloc[0]
    result.update({case_id: pm4py.fitness_token_based_replay(df, net, im, fm)['perc_fit_traces']})  # 计算适应度
    if case_id % 10 == 0:
        print(case_id)

# 比较适应度计算结果与ground_truth，计算precision、recall与f1score
thresholds = np.arange(0.5, 1.0, 0.05).tolist()
for threshold in thresholds:
    bresult = dict()
    for key, value in result.items():
        bresult.update({key: value < threshold})
    count = [0, 0, 0, 0]    # 下标是ground_truth和result组成的二进制二位数,false指正常，true指异常
    for key, value in bresult.items():
        if ground_truth[key - 1]:
            if value:
                count[3] += 1
            else:
                count[2] += 1
        else:
            if value:
                count[1] += 1
            else:
                count[0] += 1
    precision = count[0] / (count[0] + count[1])
    recall = count[0] / (count[0] + count[2])
    f1score = 2 * precision * recall / (precision + recall)
    print('threshold:' + str(threshold))
    print('precision:' + str(precision))
    print('recall:' + str(recall))
    print('f1score:' + str(f1score))
    print()
# print(result)
