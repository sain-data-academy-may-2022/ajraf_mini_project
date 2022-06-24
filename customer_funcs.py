import sys
from prettytable import PrettyTable
from database_functions import *


#-------------------------------customer GET DATA---------------------------------------------

def get_customer_name():
    try:
        name = input("Enter a name: ")
        if not name:
            print("This cannot be empty")
            return None
        else:
            return name
    except ValueError as e:
        print("This is invalid")

def get_old_customer_name():
    try:
        name = input("Enter the name you want to change: ")
        if not name:
            print("This cannot be empty")
            return None
        else:
            return name
    except ValueError:
        print("This is invalid")

def get_customer_address():
    try:
        address = input("Enter an address: ")
        if not address:
            print("This cannot be empyty")
            return None
        else:
            return address
    except ValueError:
        print("This is invalid")

def get_customer_phone():
    try:
        phone = input("Enter a phone number: ")
        if not phone:
            print("This cannot be empyty")
            return None
        elif len(phone) > 20:
            print("This number is too long")
            return None
        elif phone.isdigit() is False:
            print("Phone number can only contain digits")
            return None
        else:
            return phone
    except ValueError:

        print("This is invalid")
def get_old_customer_phone():
    try:
        phone = input("Enter the old phone number: ")
        if not phone:
            print("This cannot be empyty")
            return None
        elif len(phone) > 20:
            print("This number is too long")
            return None
        elif phone.isdigit() is False:
            print("Phone number can only contain digits")
            return None
        else:
            return phone
    except ValueError:
        
        print("This is invalid")


#------------------------CHECK UID---------------------------------------------
def check_customer_exists(name,phone):
    connection = establish_conection()
    cursor = connection.cursor()
    sql = """SELECT IF( EXISTS(
             SELECT customer_name AND customer_phone
             FROM customers
             WHERE customer_name = %s AND customer_phone = %s), 1, 0)"""
    val = (name,phone)
    cursor.execute(sql,val)
    result = cursor.fetchone()
    close_connection_and_cursor(connection,cursor)
    return result[0]
#--------------------------ADD customer------------------------------------------
def add_new_customer_to_table(name,address,phone):
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "INSERT INTO customers (customer_name,customer_address,customer_phone) VALUES (%s,%s,%s)"
    val = (name,address,phone)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

def add_new_customer():
    name = get_customer_name()
    if name == None:
        return
    address = get_customer_address()
    if address == None:
        return
    phone = get_customer_phone()
    if phone == None:
        return
    check = check_customer_exists(name,phone)
    if check == 1:
        print("This user exists")
        return
    else:
        add_new_customer_to_table(name,address,phone)
        
#-------------------CHANGE NAME,PHONE,ADDRESS----------------------------------------------


def change_customer_name():
    old_name = get_old_customer_name()
    if old_name == None:
        print("Name cannot be empty")
        return
    name = get_customer_name()
    if name == None:
        print("Name cannot be empty")
        return
    print("Now enter the phone number belonging to the user")
    phone = get_customer_phone()
    connection = establish_conection()
    cursor = connection.cursor()
    check = check_customer_exists(old_name,phone)
    if check == 1:
        sql = "UPDATE customers SET customer_name = %s WHERE customer_name = %s AND customer_phone = %s"
        val = (name,old_name, phone)
        cursor.execute(sql,val)
    else:
        print("This user does not exist")
    close_connection_and_cursor(connection,cursor)

def change_customer_address():
    name = get_customer_name()
    if name == None:
        print("Name cannot be empty")
        return
    print("Now enter the phone number belonging to the user")
    phone = get_customer_phone()
    if phone == None:
        print("Address cannot be empty")
        return
    address = get_customer_address()
    if address == None:
        print("Phone cannot be empty")
        return
    connection = establish_conection()
    cursor = connection.cursor()
    check = check_customer_exists(name,phone)
    if check == 1:
        sql = "UPDATE customers SET customer_address = %s WHERE customer_name = %s AND customer_phone = %s"
        val = (address, name, phone)
        cursor.execute(sql,val)
    else:
        print("This user does not exist")
    close_connection_and_cursor(connection,cursor)

def change_customer_phone():
    old_phone = get_old_customer_phone()
    if old_phone == None:
        print("This is invalid")
        return
    phone = get_customer_phone()
    if phone == None:
        print("This is invalid")
        return
    print("Now enter the users name associated with this number")
    name = get_customer_name()
    if name == None:
        print("This is invalid")
        return
    connection = establish_conection()
    cursor = connection.cursor()
    check = check_customer_exists(name,old_phone)
    if check == 1:
        sql = "UPDATE customers SET customer_phone = %s WHERE customer_name = %s AND customer_phone = %s"
        val = (phone, name, old_phone)
        cursor.execute(sql,val)
    else:
        print("This user does not exist")
    close_connection_and_cursor(connection,cursor)

#---------------------DELETE A customer----------------------------------------------
# def get_customer_id(name,phone):
#     connection = establish_conection()
#     cursor = connection.cursor()
#     sql = "SELECT customer_id FROM customers WHERE customer_name = %s AND customer_phone = %s "
#     val = (name,phone)
#     cursor.execute(sql,val)
#     result = cursor.fetchone()
#     if result == None:
#         print("This customer does not exist")
#         delete_a_customer()
#     else:
#         return result[0]
        
def delete_customer_from_table(name,phone):
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE customer_name = %s AND customer_phone = %s"
    val = (name,phone)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

def delete_a_customer():
    name = get_customer_name()
    if name == None:
        print("Name cannot be empty")
        return
    phone = get_customer_phone()
    if phone == None:
        print("Phone number cannot be empty")
        return
    check = check_customer_exists(name,phone)
    if check == 1:
        delete_customer_from_table(name,phone)

#-------------------------------GET DATA-----------------------------------------------------
def get_customer_id(name,phone):
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "SELECT customer_id FROM customers WHERE customer_name = %s AND customer_phone = %s"
    val = (name,phone)
    cursor.execute(sql,val)
    result =cursor.fetchone()
    close_connection_and_cursor(connection,cursor)
    return result[0]

def print_all_customers(result):
    t = PrettyTable(['Customer id', 'Customer Name', 'Customer Address','Customer Phone Number'])
    for x in result:
        t.add_row(x)
    print(t)

def view_all_customers():
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "SELECT * FROM customers"
    cursor.execute(sql)
    result = cursor.fetchall()
    print_all_customers(result)
    close_connection_and_cursor(connection,cursor)



