# Helper scripts for pinnacle DW tasks.

## Installation
paste the following commands in your terminal (on windows git bash should be used.) : 

```
git clone https://github.com/luutuankiet/pinnacle-py-utils.git &&\
cd pinnacle-py-utils &&\
python -m venv .venv &&\
pip install -r requirements.txt
 ```

## Usage
double click the scripts in folder `src` to execute the tasks below.

at first execution, the scripts will ask for certain variable inputs depending on the task, and cache to your local machine for future runs.

- checkout.py : a countdown to auto checkin / checkout innovature websites. caches username and password. **requires Firefox installed.**
- csv_diff : compares two csv files and output the differences in a .csv file. the script grabs the common columns between 2 files, and then compare the rows of the common columns to see if there are any differences.
- csv_merge : merge all .csv files in a given directory with the same columns into "combined.csv". useful to merge multiple historical files. raises AssertionError if the children csv's columns do not match.
- sql_debug : asks for a sql statement then run it in all csv files (i.e. : "select * from df"). useful to debug simple csv.
- sqlite_debug : loads all .csv file in a directory to a sqlite db. useful to debug different csv together. Extra : install SQLiteDBBrowser as client to connect to the db. Download the portable version here : https://sqlitebrowser.org/dl/