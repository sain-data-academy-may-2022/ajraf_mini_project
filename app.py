import sys
import os
from cust_items_funcs import *
from customer_funcs import *
from courier_funcs import *
from innventory_funcs import *

def courier_menu():
    while True:
        print("""This is the courier menu. \n
        [1] Add new courier \n
        [2] Change courier name \n
        [3] Change courier phone \n
        [4] Delete a courier \n
        [5] View all couriers \n
        [0] Exit
        """)
        user_option = int(input("Enter a number: "))

        match user_option:
            case 1:
                os.system('cls||clear')
                # Add a courier
                add_new_courier()
            case 2: 
                os.system('cls||clear')
                # Change courier name
                change_courier_name()
            case 3:
                os.system('cls||clear')
                # Change courier phone
                change_courier_phone()
            case 4:
                os.system('cls||clear')
                # Delete a courier
                delete_a_courier()
            case 5:
                os.system('cls||clear')
                view_all_couriers()
            case 0:
                os.system('cls||clear')
                main_menu()

def user_option_validation():
    user_option = input("Enter a number: ")
    try:
       val = int(user_option)
       return val
    except ValueError:
       print("That is not a vaild input. Please try again")
       return

def inventory_menu():
    while True:
        print("""This is the inventory menu \n
        [1] Add a new book \n
        [2] Change book name\n
        [3] Change book price \n
        [4] Delete a book \n
        [5] View all books \n
        [0] Exit
        """)
        user_option = user_option_validation()

        match user_option:
            case 1:
                os.system('cls||clear')
                add_new_book()
            case 2: 
                os.system('cls||clear')
                # Change book name
                change_book_name()
            case 3:
                os.system('cls||clear')
                # Change book price
                change_book_price()
            case 4:
                os.system('cls||clear')
                # Delete a book
                delete_book(get_book_name)
            case 5:
                os.system('cls||clear')
                # View all books
                view_all_books()
            case 0:
                main_menu()

def take_order_menu():
    while True:
        print("""This is the orders menu \n
        [1] Make new order \n
        [2] Update order \n
        [3] View all orders \n
        [4] Complete an order \n
        [0] Exit
        """)
        user_option = user_option_validation()

        match user_option:
            case 1:
                os.system('cls||clear')
                # Add a new order
                make_new_order()
            case 2: 
                os.system('cls||clear')
                # Change order
                update_order()
            case 3:
                os.system('cls||clear')
                # View all orders
                view_all_orders()
            case 4:
                os.system('cls||clear')
                # Complete order
                complete_order()
            case 0:
                os.system('cls||clear')
                main_menu()

def customer_menu():
    while True:
        print("""This is the courier menu \n
        [1] Add new customer \n
        [2] Change customer name\n
        [3] Change customer address \n
        [4] Change customer phone \n
        [5] Delete a customer \n
        [6] View all customers \n
        [0] Exit
        """)
        
        user_option = user_option_validation()

        match user_option:
            case 1:
                os.system('cls||clear')
                # Add a customer
                add_new_customer()
            case 2: 
                os.system('cls||clear')
                # Change customer name
                change_customer_name()
            case 3:
                os.system('cls||clear')
                # Change customer address
                change_customer_address()
            case 4:
                os.system('cls||clear')
                # Change customer phone
                change_customer_phone()  
            case 5:
                os.system('cls||clear')
                # Delete a customer
                delete_a_customer()
            case 6:
                os.system('cls||clear')
                view_all_customers()
            case 0:
                os.system('cls||clear')
                main_menu()

def main_menu():
    os.system('cls||clear')
    print(r"""
        ____  _ ____ ____ ____ . ____    ___  ____ ____ _  _    ____ _  _ ____ ___  
        |__|  | |__/ |__| |___ ' [__     |__] |  | |  | |_/     [__  |__| |  | |__] 
        |  | _| |  \ |  | |      ___]    |__] |__| |__| | \_    ___] |  | |__| |    
__________________________________________________________________________________________________
        """)
    print("""This is the main menu \n
    [1] Inventory Menu \n
    [2] Customers Menu \n
    [3] Couriers Menu \n
    [4] Orders Menu \n
    [0] Exit
    """)
    user_option = user_option_validation()
    match user_option:
        case 1:
            os.system('cls||clear')
            inventory_menu()
        case 2:
            os.system('cls||clear')
            customer_menu()
        case 3: 
            os.system('cls||clear')
            courier_menu()
        case 4:
            os.system('cls||clear')
            take_order_menu()
        case 0:
            os.system('cls||clear')
            print("Thanks for using the app")
            sys.exit()
        case _:
            os.system('cls||clear')
            print("This is not a valid input. Try again.")
            main_menu()
        
if __name__ == "__main__":
    main_menu()
