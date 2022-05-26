from random import randint
import json
from src.couriers import select_courier

# Creates an order from all the information collected from txt files and stores them in a dictionary
# Dictionary saved to json file

def random_with_N_digits(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

def get_details(name, address, phone):
    with open("name.txt","r") as f:
        name = f.read() 
    with open("address.txt","r") as f:
        address = f.read() 
    with open("phone.txt","r") as f:
        phone = f.read() 
    return name, address, phone

def create_dict(order_number, name, address, phone, cust_list, my_courier):
    customer_dict = {
        "order number": order_number,
        "name": name,
        "address": address,
        "phone number": phone,
        "customer order": cust_list,
        "courier": my_courier,
        "status": "In progress",
    }
    return customer_dict

def create_a_file(order_number, customer_dict):
    file_name = (str(order_number) + ".json")
    json_file = open((file_name),"w")
    json.dump(customer_dict, json_file)
    json_file.close()
    print("Your order number is:  " + str(order_number))

def create_order():
    order_number = random_with_N_digits(6)
    name, address, phone = "","",""
    name, address, phone = get_details(name, address, phone)
    cust_list = [line.strip('\n') for line in open("customer_list.txt")]
    courier = ""
    my_courier = select_courier(courier)

    customer_dict = dict()
    customer_dict = create_dict(order_number, name, address, phone, cust_list, my_courier)
    create_a_file(order_number, customer_dict)

    

