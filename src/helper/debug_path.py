import os
import sys; sys.path.append('helper')
from source_env import conf_source
# sets up the workdir

default_debug_path = conf_source('default_debug_path')
# default_debug_path = f'"{default_debug_path}"'
print(f'workdir "{default_debug_path}". input new workdir here or hit enter to confirm workdir')
user_input = input('>')
user_input = r'' + user_input
workdir = user_input or default_debug_path
os.chdir(workdir)
print(f'workdir is "{workdir}"...')
all_files = os.listdir(workdir)
# Filter out non-CSV files


# parse csv in the workdir
csv_files = [f for f in all_files if f.endswith('.csv') and f != 'combined.csv']
if csv_files == []:
    print('no csv files found. exiting...')
    raise SystemExit


delimiter = input('input the file delimiter: \n>')