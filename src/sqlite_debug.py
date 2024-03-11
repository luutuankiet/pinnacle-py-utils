#%%
import pandas as pd
from pandasql import sqldf
import os
import sqlite3
from helper import debug_path
import chardet
import numpy as np
#%%

# chardet.detect



csv_files = [file for file in os.listdir() if file.endswith('.csv')]
delimiter = input('input delimiter: ')
db_path = "debug.db"
conn = sqlite3.connect(db_path)

for csv_file in csv_files:
    print(f"Processing file: {csv_file}")
    table_name = input("Please provide table name without space :")
    
    df = pd.read_csv(csv_file,delimiter=delimiter,dtype=str)
    # df = pd.read_csv(csv_file,delimiter=delimiter,converters={i: str for i in range(100)})
    # the converters approach will not work for this case when casting to_sql to the sqlite db, because it will replace na values with '' string. use dtype to 


    # df.replace('', np.nan, inplace=True)
    
    df.to_sql(table_name,conn, index=False,if_exists='replace')

    print('table loaded.')

os.startfile("sqlitedb")