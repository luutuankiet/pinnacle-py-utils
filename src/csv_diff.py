#%%
import pandas as pd
from helper.debug_path import delimiter,csv_files
import numpy as np
import os
import csv

#%%

# checks if there are ONLY 2 files to compare
if len(csv_files)!= 2:
    print(f'can only compare with 2 files, got {len(csv_files)} files. exiting...')
    raise SystemExit


df_list = []
column_pool = []


# build the column pool
for csv_file in csv_files:
    df = pd.read_csv(csv_file,delimiter=delimiter,converters={i: str for i in range(100)})
    df.replace('', None, inplace=True)
    df_list.append(df)
    for column in list(df.columns):
        column_pool.append(column) if column not in column_pool else None


# build the unique pool
common_pool = column_pool.copy()
for df in df_list:
    for column in column_pool:
        if column not in list(df.columns):
            common_pool.remove(column)


# start diff
df1 = df_list[0][[col for col in common_pool]]
df2 = df_list[1][[col for col in common_pool]]

# Merge the two DataFrames
merged_df = pd.merge(df1, df2, indicator=True, how='outer')

# Select rows present in df1 but not in df2
unique = merged_df[(merged_df['_merge'] == 'left_only') | (merged_df['_merge'] == 'right_only')]

# lambda to flag diff columns with filename
def flag_column(value):
    if value == 'left_only':
        return csv_files[0]
    elif value == 'right_only':
        return csv_files[1]
    else:
        return 'both?'

if unique.shape[0] > 0:
    # disable the warn
    pd.options.mode.chained_assignment = None
    print('Found differences between the two files - see diff.csv for details.')
    
    unique['in_file'] = unique['_merge'].apply(flag_column).copy()

    # reorder the flag to first index
    columns = list(unique.columns)
    columns.insert(0, columns.pop(columns.index('in_file')))
    unique=unique[columns]

    # exports the csv
    unique.to_csv('diff.csv',sep='|',index=False,quotechar='"',quoting=csv.QUOTE_ALL)

else:
    print('no differences found.')

# %%
