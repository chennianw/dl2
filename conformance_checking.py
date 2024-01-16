import pm4py
import pandas as pd
import csv
import numpy as np


def is_abnormal(event_log, net, im, fm, threshold):
    fitness = pm4py.fitness_alignments(event_log, net, im, fm)['averageFitness']
    return fitness >= threshold


# file_path = 'test.csv'
# event_log = pm4py.format_dataframe(pd.read_csv(file_path), case_id='c', activity_key='e', timestamp_key='ws')
net, im, fm = pm4py.read_pnml('test.pnml')
# print(is_abnormal(event_log, net, im, fm, 0.8))

# F = pm4py.fitness_alignments(event_log, net, im, fm)
# fitness = pm4py.fitness_alignments(event_log, net, im, fm)['averageFitness']
# precision = pm4py.precision_alignments(event_log, net, im, fm)
# f1score = 2 * fitness * precision / (fitness + precision)
# print('fitness:' + str(fitness))
# print('precision:' + str(precision))
# print('f1score:' + str(f1score))

test_file_path = 't.csv'
ground_truth_path = 't.csv'
test_event_log = pm4py.format_dataframe(pd.read_csv(test_file_path), case_id='c', activity_key='e', timestamp_key='t')
ground_truth = pd.read_csv(ground_truth_path)
dfs = [group for _, group in test_event_log.groupby('c')]
thresholds = np.arange(0.5, 1.0, 0.05).tolist()
result = dict()
for threshold in thresholds:
    for df in dfs:
        result.update({df['c'].iloc[0]: is_abnormal(df, net, im, fm, threshold)})
print()
