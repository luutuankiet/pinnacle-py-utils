#%%
import pandas as pd
from pandasql import sqldf
import os
import sqlite3
from helper import debug_path
import chardet
import numpy as np
import venv
import subprocess
#%%

# chardet.detect
# default_path = os.getcwd()
# print(f'workdir "{default_path}". input new workdir here or hit enter to confirm workdir')
# user_input = input('>')
# user_input = r'' + user_input
# workdir = user_input or default_path
# print(f'workdir is "{workdir}"...')
# os.chdir(workdir)

#%%

csv_files = [file for file in os.listdir() if file.endswith('.csv')]
delimiter = input('input delimiter: ')
db_path = "debug.db"
conn = sqlite3.connect(db_path)

for csv_file in csv_files:
    print(f"Processing file: {csv_file}")
    table_name = input("Please provide table name without space :")
    
    df = pd.read_csv(csv_file,delimiter=delimiter,converters={i: str for i in range(100)})
    # although the converters approach parses na values as empty string, use it to confidently create the sqlite db as raw data. Cases: there's freetext fields with na, n/a, NA etc. which this approach will consistently parse allthem as raw
    df.replace('', np.nan, inplace=True)
    # additional step to process true empty string, not na strings
    
    df.to_sql(table_name,conn, index=False,if_exists='replace')

    print('table loaded.')

open_sqlitedb = input('processing done. open with sqlite?(y/n)')

if open_sqlitedb == 'y':
    db_path = os.path.join(os.getcwd(),'debug.db')
    # os.startfile(f"sqlitedb {db_path}")
    sqlite_bin = r'Z:\utils\SQLiteDatabaseBrowserPortable\SQLiteDatabaseBrowserPortable.exe'
    command = [sqlite_bin,db_path]
    subprocess.call(command)