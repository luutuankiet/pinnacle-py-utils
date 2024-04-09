#%%
import json
import os



# parse from the conf dir
SOURCE_DIR = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(SOURCE_DIR,'config.json')


with open(CONFIG_FILE, 'a+') as f:
    # move cursor to top
    f.seek(0)

    # Load JSON data if file is not empty, otherwise initialize with empty dictionary
    try:
        conf = json.load(f)
    except json.JSONDecodeError:
        conf = {}


def conf_source(*params):
    """ dynamically returns the value for the params, creating on the fly if not found  """
    input_values = {}
    for param in params:
        value = conf.get(param)
        if value is None:
            value = input(f'"{param}" not found in cache. Enter "{param}" to set up: ')
            conf[param] = value
            with open(CONFIG_FILE, 'w') as f:
                json.dump(conf, f, indent=4)
    return tuple(conf.get(param) for param in params)
# %%
