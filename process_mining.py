import pm4py
import pandas as pd
import csv
import numpy as np

# # 模拟过程挖掘
# file_path = 'data/bpic12.csv'
# event_log = pm4py.format_dataframe(pd.read_csv(file_path), case_id='Case ID', activity_key='Activity', timestamp_key='ws')

# thresholds = [0, 0.5, 1]
# dependency_threshold = 0.5
# and_threshold = 0.65
# loop_two_threshold = 0.5
# for dependency_threshold in thresholds:
#     for and_threshold in thresholds:
#         for loop_two_threshold in thresholds:
#             net, im, fm = pm4py.discover_petri_net_heuristics(event_log, dependency_threshold=dependency_threshold, and_threshold=and_threshold, loop_two_threshold=loop_two_threshold)
#             pm4py.write_pnml(net, im, fm, 'process_model/heuristics_' + str(dependency_threshold) + '_' + str(and_threshold) + '_' + str(loop_two_threshold) + '.pnml')
#
# thresholds = [0, 0.25,  0.5, 0.75, 1]
# for noise_threshold in thresholds:
#     for disable_fallthroughs in [False, True]:
#         net, im, fm = pm4py.discover_petri_net_inductive(event_log, noise_threshold=noise_threshold, disable_fallthroughs=disable_fallthroughs)
#         pm4py.write_pnml(net, im, fm, 'process_model/inductive_' + str(noise_threshold) + '_' + str(disable_fallthroughs) + '.pnml')
#
# thresholds = [0, 0.25,  0.5, 0.75, 1]
# for alpha in thresholds:
#     net, im, fm = pm4py.discover_petri_net_ilp(event_log, alpha=alpha)
#     pm4py.write_pnml(net, im, fm, 'process_model/ilp_' + str(alpha) + '.pnml')

# 过程挖掘
file_path = 'data/normal_patient.csv'
df = pd.read_csv(file_path)
df = df[df['c'] < 600]
event_log = pm4py.format_dataframe(df, case_id='c', activity_key='e', timestamp_key='t')
net, im, fm = pm4py.discover_petri_net_heuristics(event_log)
pm4py.write_pnml(net, im, fm, 'data/normal_heuristics_part.pnml')