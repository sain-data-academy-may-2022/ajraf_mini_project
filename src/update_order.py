import json
import os
from src.create_menu_list import create_list
from src.print_menu import change_menu
from src.complete import complete_order
from src.delete_order import delete_order

# Opens json file into new dictioary. Edits dictionary. Rewrites the file upon completion

def change_values(get_order,data):
    change_input = int(input("Enter a number: "))
    match change_input:
        case 1:
            dict_value = "name"
            data[dict_value] = input("Enter a new name: ")
        case 2:
            dict_value = "address"
            data[dict_value] = input("Enter a new addres: s")
        case 3:
            dict_value = "phone number"
            data[dict_value] = input("Enter a new phone number: ")
        case 4:
            dict_value = "customer order"
            create_list()
            cust_list = [line.strip('') for line in open("customer_list.txt")]
            data[dict_value] = cust_list
        case 5: 
            dict_value = "status"
            data[dict_value] = "Completed"
            complete_order(get_order)
            #delete_order(get_order)
        

def update_order():
    get_order = input("Enter order number: ")
    order_json_file = (get_order+".json")

    with open(order_json_file, "r") as jsonFile:
        data = json.load(jsonFile)

    change_menu()
    change_values(get_order,data)
    
    with open(order_json_file, "w") as jsonFile:
        json.dump(data, jsonFile)