#%%
import pandas as pd
from pandasql import sqldf
import os
import code
from helper import debug_path
import numpy as np
import venv
#%%

default_path=r'C:\Users\ep.kl1406\Downloads\debug'
cwd=input(f'default dir {default_path}, or input path here:')
if cwd=='':
    cwd=default_path
delimiter = input('input delimiter: ')
db=[]
os.chdir(cwd)
def sql_debug(query="select * from df",delim=delimiter):
    csv_files = [file for file in os.listdir(cwd) if file.endswith('.csv')]
    while query:
        global db
        db = []
        for file in csv_files:
            print(file)
            df = pd.read_csv(file,delimiter=delim,converters={i: str for i in range(100)})
            # although the converters approach parses na values as empty string, use it to confidently create the sqlite db as raw data. Cases: there's freetext fields with na, n/a, NA etc. which this approach will consistently parse allthem as raw
            df.replace('', np.nan, inplace=True)
            # additional step to process true empty string, not na strings
    
            try:
                print(sqldf(query))
            except Exception as e:
                print(f"error : {e}")
            # from pdb import set_trace; set_trace()
            print('-' * 8 + '\n\n\n')
            db.append(df)
        for i,file in enumerate(csv_files):
            print(f'df {file} added to pos {i} of db')
        query=input('input query:')
sql_debug()


code.interact(local=locals())
