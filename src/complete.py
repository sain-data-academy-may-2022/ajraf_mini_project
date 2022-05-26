from json import dump, load
import json
from pathlib import Path

def add_to_file(order_number):
    with open("completed.json", "r") as f:
        old_data = json.load(f)
            
    with open(f"{order_number}.json","r") as f:
        data = json.load(f)
            
    old_data.append(data)
    with open("completed.json","w") as fp:
        json.dump(old_data, fp)

def create_a_file(order_number, new_list):
    with open(f"{order_number}.json","r") as f:
        data = json.load(f)
    new_list.append(data)
    with open("completed.json","w") as fp:
        json.dump(data, fp)

def complete_order(get_order):
    order_number = get_order
    path_to_file = "completed.json"
    path = Path(path_to_file)
    new_list = []

    if path.is_file():
        add_to_file(order_number)
    else:
        create_a_file(order_number, new_list)


    

    
   



