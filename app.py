import sys

from src.create_menu_list import create_list
from src.customer_data import customer_data
from src.create_order import create_order
from src.update_order import update_order
from src.delete_order import delete_order
from src.print_menu import main_print
from src.view import view_all
from view_completed import view

# Fuctions imported from python files
# Menu created with pattern matching

def menu_options():
    user_input = int(input("Enter a menu input: "))
    match user_input:
        case 1:
            print("\033c")
            create_list()
            menu()
        case 2:
            print("\033c")
            customer_data()
            menu()
        case 3:
            print("\033c")
            create_order()
            menu()
        case 4:
            print("\033c")
            update_order()
            menu()
        case 5:
            print("\033c")
            delete_order()
            menu()
        case 6:
            print("\033c")
            view_all()
            menu()
        case 7:
            view()
            pass
        case 0:
            sys.exit()
        case _:
            print("That didn't work. Try again.")
            menu()

def menu():
    print("\033c")
    while True:
        main_print()
        menu_options()

menu()