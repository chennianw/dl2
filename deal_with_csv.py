import pandas
import csv
import numpy

old_df = pandas.read_csv('test.csv')
new_df = old_df[['c', 'e', 'ws']]
new_df = new_df.rename(columns={"ws": "t"})
x = len(new_df)
random_values = numpy.random.randint(2, size=x)
series = pandas.Series(random_values)
new_df['r'] = series
case_id = 0
random_value = 0
for index, row in new_df.iterrows():
    if row['c'] != case_id:
        random_value = numpy.random.randint(2)
        case_id = row['c']
    new_df.at[index, 'r'] = random_value
new_df.to_csv('t.csv')
