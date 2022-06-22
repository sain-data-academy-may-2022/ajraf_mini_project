
from prettytable import PrettyTable
import sys
from database_functions import *

def inventory_menu():
    print("""This is the orders menu \n
    [1] Add a new book \n
    [2] Change book name\n
    [3] Change book price \n
    [4] Delete a book \n
    [5] View all books \n
    [0] Exit
    """)
    user_option = int(input("Enter a number: "))

    match user_option:
        case 1:
            add_new_book()
        case 2: 
            # Change book name
            change_book_name()
        case 3:
            # Change book price
            change_book_price()
        case 4:
            # Delete a book
            pass
        case 5:
            # View all books
            view_all_books()
        case 0:
            sys.exit()
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
    quantity = get_book_quantity()
    price = get_book_price()
    check = check_name_in_table(name)
    if check == 1:
        print("This item already exists")
        inventory_menu()
    else:
        add_new_book_to_table(name,quantity,price)

def get_book_name():
    try:
        name = input("Enter a book name: ")
    except ValueError as e:
        print(e)
    return name

def get_book_quantity():
    try:
        quantity = int(input("Enter the quantity: "))
    except ValueError as e:
        print(e)
    return quantity

def get_book_price():
    try:
        price = float(input("Enter the price: "))
    except ValueError as e:
        print(e)
    return price

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
    t = PrettyTable(['Book id', 'Book Name', 'Quantity','Price','OOS'])
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
    id_name_quantity = get_book_to_change(book)
    id,name,quantity = id_name_quantity
    price = get_book_price()
    update_old_oos_book(id,book)
    add_new_book_to_table(name,quantity,price)


inventory_menu()
