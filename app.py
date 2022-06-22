import sys
from cust_items_funcs import take_order_menu
from customer_funcs import customer_menu
from courier_funcs import courier_menu
from innventory_funcs import inventory_menu

def main_menu():
    print("""This is the main menu \n
    [1] Inventory Menu \n
    [2] Customers Menu \n
    [3] Couriers Menu \n
    [4] Orders Menu \n
    [0] Exit
    """)
    user_option = input("Enter a number: ")
    if isinstance(user_option, int):
        while True:
            match user_option:
                case 1:
                    inventory_menu()
                case 2:
                    customer_menu()
                case 3: 
                    courier_menu()
                case 4:
                    take_order_menu()
                case 0:
                    sys.exit()
                case _:
                    main_menu()
    else:
        sys.exit()

    
        
if __name__ == "__main__":
    main_menu()
