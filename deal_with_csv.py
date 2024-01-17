import pandas
import csv
import numpy
import pm4py

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

df = pandas.read_csv('bpic12.csv')
event_log = pm4py.format_dataframe(df, case_id='Case ID', activity_key='Activity', timestamp_key='ws')
log = pm4py.convert_to_event_log(event_log)
pm4py.objects.log.exporter.xes.exporter.apply(log, 'bpic12.xes')

