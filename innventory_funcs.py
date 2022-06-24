from prettytable import PrettyTable
import sys
from database_functions import *

#----------------------CHECK AGAINST bookS--------------------------
def check_name_in_table(name):
    connection = establish_conection()
    cursor = connection.cursor()
    book_name = name
    sql = """SELECT IF( EXISTS(
             SELECT book_name
             FROM books
             WHERE book_name = %s AND book_oos = 'N'), 1, 0)"""
    val = (book_name)

    cursor.execute(sql,val)
    result = cursor.fetchone()
    close_connection_and_cursor(connection,cursor)
    return result[0]

# -----------------------ADD bookS ----------------------------------
def add_new_book_to_table(name,quantity,price):
    connection = establish_conection()
    cursor = connection.cursor()
    name,quantity,price = name,quantity,price
    sql = "INSERT INTO books (book_name,book_price,book_quantity,book_oos) VALUES (%s,%s,%s,%s)"
    val = (name,price,quantity, "N")
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

def add_new_book():
    name = get_book_name()
    if name is None:
        print("Enter a valid name")
        return  
    check = check_name_in_table(name)
    if check == 1:
        print("This item already exists")
        return
    quantity = get_book_quantity()
    if quantity is None:
        print("This is not valid. Returning you to menu")
        return
    price = get_book_price()
    if price is None:
        print("This is not valid. Returning you to menu")
        return
    add_new_book_to_table(name,quantity,price)

def get_book_name():
    try:
        name = input("Enter a book name: ")
        if name == "":
            return None
        return name
    except ValueError as e:
        print(e)
    

def get_book_quantity():
    quantity = input("Enter the quantity: ")
    try:
        quantity = int(quantity)
        if quantity < 0:
            return None
        return quantity
    except ValueError as e:
        return None

def get_book_price():
    price = input("Enter the price: ")
    try:
        price = float(price)
        if price < 0:
            return None
        return price
    except ValueError as e:
        return None

# -------------------------------CHNAGE BOOK NAME--------------------------------------------
def update_book_name_on_table(new_name, old_name):
    connection = establish_conection()
    cursor = connection.cursor()
    name = new_name
    old_name = old_name
    sql = "UPDATE books SET book_name = %s WHERE book_name = %s"
    val = (name, old_name)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

def change_book_name():
    print("Enter the book you want to change")
    old_name = get_book_name()
    check = check_name_in_table(old_name)
    if check == 1:
        print("Please enter the new name")
        new_name = get_book_name()
        update_book_name_on_table(new_name,old_name)
    else:
        print("This item does not exist")

#---------------------------------------------------------------------------------------------
def print_all_books(result):
    t = PrettyTable(['Book id', 'Book Name', 'Price','Quantity','OOS'])
    for x in result:
        t.add_row(x)
    print(t)

def view_all_books():
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "SELECT * FROM books WHERE book_oos = 'N'"
    cursor.execute(sql)
    result = cursor.fetchall()
    print_all_books(result)
    close_connection_and_cursor(connection,cursor)

#--------------------------------CHANGE PRICE--------------------------------------------------------------
def get_book_to_change(book):
    book = book
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "SELECT * FROM books WHERE book_name = %s AND book_oos = 'N'"
    val = (book)
    cursor.execute(sql,val)
    result = cursor.fetchone()
    book_id, book_name,book_price,book_quantity,book_oos = result
    close_connection_and_cursor(connection,cursor)
    return book_id,book_name,book_quantity

def update_old_oos_book(id,book):
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "UPDATE books SET book_oos = 'Y' WHERE book_id = %s"
    val = (id)
    cursor.execute(sql,val)
    sql = "UPDATE books SET book_name = 'OOS' WHERE book_name = %s"
    val = (book)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

def change_book_price():
    book = get_book_name()
    if book == None:
        print("This is invalid")
        return
    id_name_quantity = get_book_to_change(book)
    id,name,quantity = id_name_quantity
    price = get_book_price()
    update_old_oos_book(id,book)
    add_new_book_to_table(name,quantity,price)

#---------------------DELETE BOOK-------------------------------------
def delete_book_from_table(name):
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "DELETE FROM books WHERE book_name = %s"
    val = (name)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

def delete_book(get_book_name):
    name = get_book_name()
    if name is None:
        print("Enter a valid book name")
        return 
    delete_book_from_table(name)
    
