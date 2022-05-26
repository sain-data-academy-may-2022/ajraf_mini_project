import json
from pprint import pprint

def view():
    with open("completed.json", "r") as file:
        data =json.load(file)
    pprint(data, sort_dicts=False, indent=1)