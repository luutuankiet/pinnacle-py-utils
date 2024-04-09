import pandas as pd
import os
from helper.debug_path import delimiter,csv_files,workdir
import csv



# Create a list to hold the dataframes
df_list = []

for csv_file in csv_files:
    file_path = os.path.join(workdir, csv_file)
    print(f'processing file {csv_file}...')
    try:
        # Try reading the file using default UTF-8 encoding
        df = pd.read_csv(file_path,delimiter=delimiter,converters={i: str for i in range(100)})
        # !!!! important to use converters because it will translate na values from df to '' string
        df_list.append(df)
    except UnicodeDecodeError:
        try:
            # If UTF-8 fails, try reading the file using UTF-16 encoding with tab separator
            df = pd.read_csv(file_path, sep=delimiter, encoding='utf-16')
            df_list.append(df)
        except Exception as e:
            print(f"Could not read file {csv_file} because of error: {e}")
    except Exception as e:
        print(f"Could not read file {csv_file} because of error: {e}")
big_df = pd.concat(df_list, ignore_index=True)

# validation
ref_columns=list(df_list[1].columns)
ref_dtypes=df_list[1].dtypes.to_dict()
for i,df in enumerate(df_list):
    assert list(df.columns) == ref_columns,f'column names in df {i} is different.'

    assert df.dtypes.to_dict() == ref_dtypes,f'dtypes in df {i} is different.'
    
big_df.to_csv(os.path.join(workdir, 'combined.csv'), sep=delimiter, index=False,quoting=csv.QUOTE_ALL)
print(f'sucessfully merged to csv with the following snippet : \n\n\n{big_df} \n\n\n{big_df.dtypes}')
input('hit enter to close this script.')