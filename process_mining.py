import pm4py
import pandas as pd
import csv
import numpy as np

file_path = 'test.csv'
event_log = pm4py.format_dataframe(pd.read_csv(file_path), case_id='c', activity_key='e', timestamp_key='ws')
net, im, fm = pm4py.discover_petri_net_heuristics(event_log)
pm4py.write_pnml(net, im, fm, 'test.pnml')
