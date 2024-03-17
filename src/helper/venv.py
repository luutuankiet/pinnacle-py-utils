import os

# Get the absolute path to the 'activate_this.py' script
activator = os.path.abspath('activate_this.py')

# Read the content of the 'activate_this.py' script
with open(activator, 'r') as f:
    script_content = f.read()

# Execute the content of the script using exec()
# Pass '__file__' as a key-value pair in the local namespace
exec(script_content, {'__file__': activator})
