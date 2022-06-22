import sys
from prettytable import PrettyTable
from database_functions import *

def customer_menu():
    print("""This is the courier menu \n
    [1] Add new customer \n
    [2] Change customer name\n
    [3] Change customer address \n
    [4] Change customer phone \n
    [5] Delete a customer \n
    [6] View all customers \n
    [0] Exit
    """)
    user_option = int(input("Enter a number: "))

    match user_option:
        case 1:
            # Add a customer
            add_new_customer()
        case 2: 
            # Change customer name
            change_customer_name()
        case 3:
            # Change customer address
            change_customer_address()
        case 4:
            # Change customer phone
            change_customer_phone()  
        case 5:
            # Delete a customer
            delete_a_customer()
        case 6:
            view_all_customers()
        case 0:
            sys.exit()
#-------------------------------customer GET DATA---------------------------------------------

def get_customer_name():
    try:
        name = input("Enter a name: ")
    except ValueError as e:
        print(e)
    return name

def get_customer_address():
    try:
        address = input("Enter an address: ")
    except ValueError as e:
        print(e)
    return address

def get_customer_phone():
    try:
        phone = input("Enter a phone number: ")
    except ValueError as e:
        print(e)
    return phone

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
    address = get_customer_address()
    phone = get_customer_phone()
    check = check_customer_exists(name,phone)
    if check == 1:
        print("This user exists")
        customer_menu()
    else:
        add_new_customer_to_table(name,address,phone)
        
#-------------------CHANGE NAME,PHONE,ADDRESS----------------------------------------------


def change_customer_name():
    old_name = input("Enter the old name: ")
    name = get_customer_name()
    print("Now enter the phone number belonging to the user")
    phone = get_customer_phone()
    connection = establish_conection()
    cursor = connection.cursor()
    check = check_customer_exists(name,phone)
    if check == 1:
        sql = "UPDATE customers SET customer_name = %s WHERE customer_name = %s AND customer_phone = %s"
        val = (name,old_name, phone)
        cursor.execute(sql,val)
    else:
        print("This user does not exist")
    close_connection_and_cursor(connection,cursor)

def change_customer_address():
    name = get_customer_name()
    print("Now enter the phone number belonging to the user")
    phone = get_customer_phone()
    address = get_customer_address()
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
    old_phone = input("Enter the old phone: ")
    phone = get_customer_phone()
    print("Now enter the users name associated with this number")
    name = get_customer_name()
    connection = establish_conection()
    cursor = connection.cursor()
    check = check_customer_exists(name,phone)
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
    phone = get_customer_phone()
    check = check_customer_exists(name,phone)
    if check == 1:
        #cid = get_customer_id()
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



customer_menu()