import pandas as pd
import os
from helper import debug_path
import chardet
import venv

# >>> import urllib.request
# >>> rawdata = urllib.request.urlopen('http://yahoo.co.jp/').read()
# >>> import chardet
# >>> chardet.detect(rawdata)
# {'encoding': 'EUC-JP', 'confidence': 0.99}


# replace with your folder's path
default_path = os.getcwd()
print(f'setting default path as current dir at {default_path}. \nhit enter to confirm or insert new folder path: ')
user_input=input('>')

delimiter=input('input the file delimiter: \n>')
folder_path = user_input.strip() or default_path
all_files = os.listdir(folder_path)

# Filter out non-CSV files
csv_files = [f for f in all_files if f.endswith('.csv') and f != 'combined.csv' ]

# Create a list to hold the dataframes
df_list = []

for csv in csv_files:
    file_path = os.path.join(folder_path, csv)
    print(f'processing file {csv}...')
    try:
        # Try reading the file using default UTF-8 encoding
        df = pd.read_csv(file_path,delimiter=delimiter,converters={i: str for i in range(100)})
        df_list.append(df)
    except UnicodeDecodeError:
        try:
            # If UTF-8 fails, try reading the file using UTF-16 encoding with tab separator
            df = pd.read_csv(file_path, sep=delimiter, encoding='utf-16')
            df_list.append(df)
        except Exception as e:
            print(f"Could not read file {csv} because of error: {e}")
    except Exception as e:
        print(f"Could not read file {csv} because of error: {e}")
big_df = pd.concat(df_list, ignore_index=True)

# validation
ref_columns=list(df_list[1].columns)
ref_dtypes=df_list[1].dtypes.to_dict()
for i,df in enumerate(df_list):
    assert list(df.columns) == ref_columns,f'column names in df {i} is different.'

    assert df.dtypes.to_dict() == ref_dtypes,f'dtypes in df {i} is different.'
    
# big_df.to_csv(os.path.join(folder_path, 'combined.csv'), sep='|', index=False,float_format='raw',date_format='raw')
big_df.to_csv(os.path.join(folder_path, 'combined.csv'), sep=delimiter, index=False)
print(f'sucessfully merged to csv with the following snippet : \n\n\n{big_df} \n\n\n{big_df.dtypes}')
input('hit enter to close this script.')