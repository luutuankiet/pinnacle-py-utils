import pandas as pd
from pandasql import sqldf
import os
import sqlite3
from helper import debug_path


csv_files = [file for file in os.listdir() if file.endswith('.csv')]
delimiter = input('input delimiter: ')
db_path = "debug.db"
conn = sqlite3.connect(db_path)

for csv_file in csv_files:
    print(f"Processing file: {csv_file}")
    table_name = input("Please provide table name without space :")
    
    df = pd.read_csv(csv_file,delimiter=delimiter,converters={i: str for i in range(100)})
    
    df.to_sql(table_name,conn, index=False,if_exists='replace')

    print('table loaded.')

os.startfile("sqlitedb")