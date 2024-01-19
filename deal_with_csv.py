import pandas as pd
import csv
import numpy as np
import pm4py
from datetime import datetime

# # 模拟数据
# old_df = pandas.read_csv('test.csv')
# new_df = old_df[['c', 'e', 'ws']]
# new_df = new_df.rename(columns={"ws": "t"})
# x = len(new_df)
# random_values = numpy.random.randint(2, size=x)
# series = pandas.Series(random_values)
# new_df['r'] = series
# case_id = 0
# random_value = 0
# for index, row in new_df.iterrows():
#     if row['c'] != case_id:
#         random_value = numpy.random.randint(2)
#         case_id = row['c']
#     new_df.at[index, 'r'] = random_value
# new_df.to_csv('t.csv')

# # 模拟ground_truth
# df = pandas.read_csv('bpic12.csv')
# event_log = pm4py.format_dataframe(df, case_id='Case ID', activity_key='Activity', timestamp_key='ws')
# new_df = df[['Case ID']].drop_duplicates(keep='first').reset_index().drop('index', axis=1)
# x = len(new_df)
# random_values = numpy.random.randint(2, size=x)
# series = pandas.Series(random_values)
# new_df['r'] = series
# new_df.to_csv('ground_truth.csv')

# # csv转xes
# df = pd.read_csv('patient.csv')
# event_log = pm4py.format_dataframe(df, case_id='c', activity_key='e', timestamp_key='t')
# log = pm4py.convert_to_event_log(event_log)
# pm4py.objects.log.exporter.xes.exporter.apply(log, 'patient.xes')

# 获取ground_truth
ground_truth_path = 'data/gold_standard.csv'
df = pd.read_csv(ground_truth_path)
ground_truth = []
for index, row in df.iterrows():
    ground_truth.append(row['1dAVb'] + row['RBBB'] + row['LBBB'] + row['SB'] + row['AF'] + row['ST'] > 0)

# 将trace拼成事件日志
total_df = pd.DataFrame()
for i in range(1, 828):
    test_file_path = 'events/events/patient_' + str(i) + '.csv'
    df = pd.read_csv(test_file_path)
    if len(df) == 0:
        continue
    df = df.assign(c=str(i))
    df['t'] = df['end_time_steps'].apply(datetime.utcfromtimestamp)
    df['e'] = df['events'].astype(str)
    total_df = pd.concat([total_df, df])
total_df.to_csv('data/patient.csv')

total_df = pd.DataFrame()
for i in range(1, 828):
    if not ground_truth[i - 1]:
        test_file_path = 'events/events/patient_' + str(i) + '.csv'
        df = pd.read_csv(test_file_path)
        if len(df) == 0:
            continue
        df = df.assign(c=str(i))
        df['t'] = df['end_time_steps'].apply(datetime.utcfromtimestamp)
        df['e'] = df['events'].astype(str)
        total_df = pd.concat([total_df, df])
total_df.to_csv('data/normal_patient.csv')

total_df = pd.DataFrame()
for i in range(1, 828):
    if ground_truth[i - 1]:
        test_file_path = 'events/events/patient_' + str(i) + '.csv'
        df = pd.read_csv(test_file_path)
        if len(df) == 0:
            continue
        df = df.assign(c=str(i))
        df['t'] = df['end_time_steps'].apply(datetime.utcfromtimestamp)
        df['e'] = df['events'].astype(str)
        total_df = pd.concat([total_df, df])
total_df.to_csv('data/abnormal_patient.csv')
