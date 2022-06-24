from prettytable import PrettyTable
from database_functions import *

#-------------------------------courier GET DATA---------------------------------------------

def get_courier_name():
    try:
        name = input("Enter a name: ")
        if not name:
            print("This cannot be empyty")
            return None
        else:
            return name
    except ValueError as e:
        print(e)

def get_courier_phone():
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
    except ValueError as e:
        print(e)

def get_random_courier():
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "SELECT courier_id FROM couriers ORDER BY RAND() LIMIT 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    close_connection_and_cursor(connection,cursor)
    return result[0]

def print_all_couriers(result):
    t = PrettyTable(['Couriers id', 'Courier Name', 'Courier Phone Number','Courier Company'])
    for x in result:
        t.add_row(x)
    print(t)

def view_all_couriers():
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "SELECT * FROM couriers"
    cursor.execute(sql)
    result = cursor.fetchall()
    print_all_couriers(result)
    close_connection_and_cursor(connection,cursor)

#------------------------CHECK UID---------------------------------------------
def check_if_courier_exists(name,phone):
    connection = establish_conection()
    cursor = connection.cursor()
    sql = """SELECT IF( EXISTS(
             SELECT courier_name AND courier_phone
             FROM couriers
             WHERE courier_name = %s AND courier_phone = %s), 1, 0)"""
    val = (name,phone)
    cursor.execute(sql,val)
    result = cursor.fetchone()
    close_connection_and_cursor(connection,cursor)
    return result[0]
#--------------------------ADD courier------------------------------------------
def add_new_courier_to_table(name,phone,company):
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "INSERT INTO couriers (courier_name,courier_phone,courier_company) VALUES (%s,%s,%s)"
    val = (name,phone,company)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

def add_new_courier():
    company = "Royal Mail"
    name = get_courier_name()
    if name == None:
        return
    phone = get_courier_phone()
    if phone == None:
        return
    check = check_if_courier_exists(name,phone)
    if check == 1:
        print("This user exists")
        return
    else:
        add_new_courier_to_table(name,phone,company)
        
#-------------------CHANGE NAME,PHONE,ADDRESS----------------------------------------------
   
def change_courier_name():
    old_name = input("Enter the old name: ")
    name = get_courier_name()
    phone = get_courier_phone()

    connection = establish_conection()
    cursor = connection.cursor()
    sql = "UPDATE couriers SET courier_name = %s WHERE courier_name = %s AND courier_phone = %s"
    val = (name, old_name, phone)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

def change_courier_phone():
    name = get_courier_name()
    old_phone = input("Enter the old phone number: ")
    phone = get_courier_phone()
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "UPDATE couriers SET courier_phone = %s WHERE courier_name = %s AND courier_phone = %s"
    val = (phone, name, old_phone)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

#---------------------DELETE A courier----------------------------------------------
def delete_courier_from_table(name,phone):
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "DELETE FROM couriers WHERE courier_name = %s AND courier_phone = %s"
    val = (name,phone)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

def delete_a_courier():
    name = get_courier_name()
    phone = get_courier_phone()
    check = check_if_courier_exists(name,phone)
    if check == 1:
        delete_courier_from_table(name,phone)

#------------------------------------------------------------------------------------
