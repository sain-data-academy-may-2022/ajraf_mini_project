import json
from glob import glob

# Creates a list of all json files and prints the conents.

def view_all():
    data = []
    for file_name in glob('*.json'):
        with open(file_name) as f:
            data.append(json.load(f))
            print(json.dumps(data, indent=4, sort_keys=False))



