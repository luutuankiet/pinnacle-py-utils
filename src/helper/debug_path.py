import os

debug_path = r'Z:\downloads\debug'
print(f'workdir "{debug_path}". input new workdir here or hit enter to confirm workdir')
user_input = input('>')
user_input = r'' + user_input
workdir = user_input or debug_path
os.chdir(workdir)
print(f'workdir is "{workdir}"...')
