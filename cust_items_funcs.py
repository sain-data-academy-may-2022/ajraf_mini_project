from prettytable import PrettyTable
from database_functions import *
import sys
from customer_funcs import *
from courier_funcs import get_random_courier

def create_order(customer_id,courier_id):
    connection = establish_conection()
    cursor = connection.cursor()
    sql ="INSERT INTO orders (customer_id,courier_id,final_price) VALUES (%s,%s,%s)"
    val = (customer_id,courier_id,0.0)
    cursor.execute(sql,val)
    sql = "SELECT * FROM orders ORDER BY order_id DESC LIMIT 1"
    cursor.execute(sql)
    result = cursor.fetchone()
    close_connection_and_cursor(connection,cursor)
    return result[0]

def take_order_menu():
    print("""This is the orders menu \n
    [1] Make new order \n
    [2] Update order \n
    [3] View all orders \n
    [4] Complete an order \n
    [0] Exit
    """)
    user_option = int(input("Enter a number: "))

    match user_option:
        case 1:
            # Add a new order
            make_new_order()
        case 2: 
            # Change order
            update_order()
        case 3:
            # View all orders
            view_all_orders()
        case 4:
            # Complete order
            complete_order()
        case 0:
            sys.exit()

#----------------------------------------GET DATA------------------------------------------------------------------
def get_all_order_items(order_id):
    order = order_id
    connection = establish_conection()
    cursor = connection.cursor()
    sql = """
    select book_name,sum(book_quantity)
    from customer_order 
    where order_id = %s
    group by book_name
    """
    val = (order)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close_connection_and_cursor(connection,cursor)
    return result

def get_all_order_prices(order_id):
    order = order_id
    connection = establish_conection()
    cursor = connection.cursor()
    sql = """
    select book_name,locked_price
    from customer_order 
    where order_id = %s
    """
    val = (order)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close_connection_and_cursor(connection,cursor)
    return result

get_all_order_items(51)
def get_price(item):
    connection = establish_conection()
    cursor = connection.cursor()
    valid_item = item
    sql = "SELECT book_price FROM books WHERE book_name = %s"
    val = (valid_item)
    cursor.execute(sql,val)
    result = cursor.fetchone()
    close_connection_and_cursor(connection,cursor)
    return result[0]
#-------------------------------------------CHECK ID----------------------------------------------------------
def check_customer_id(name,phone):
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "SELECT customer_id FROM customers WHERE customer_name = %s AND customer_phone = %s "
    val = (name,phone)
    cursor.execute(sql,val)
    result = cursor.fetchone()
    if result == None:
        print("This customer does not exist")
        make_new_order()
    else:
        return result[0]
#-----------------------------------------ADD DATA TO TABLE---------------------------------------------------------
def add_to_customer_items_table(order_id,item,quantity,locked_price,total_price):
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "INSERT INTO customer_order (order_id,book_name,book_quantity,locked_price,total_price) VALUES (%s,%s,%s,%s,%s)"
    val = (order_id,item,quantity,locked_price,total_price)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

def check_if_item_exists(item):
    connection = establish_conection()
    cursor = connection.cursor()
    valid_item = item
    sql = """SELECT IF( EXISTS(
             SELECT book_name
             FROM customer_order
             WHERE book_name = %s), 1, 0)"""
    val = (valid_item)
    cursor.execute(sql,val)
    result = cursor.fetchone()
    close_connection_and_cursor(connection,cursor)
    return result[0]

# def update_the_order(order_id,quantity,total_price):
#     quantity = quantity
#     connection = establish_conection()
#     cursor = connection.cursor()
#     sql = "UPDATE customer_order SET book_quantity = (book_quantity + %s) AND total_price = (total_price + %s) WHERE order_id = %s"
#     val = (quantity,total_price,order_id)
#     cursor.execute(sql,val)
#     close_connection_and_cursor(connection,cursor)

def assemble_customer_items(order_id,item,quantity):
    item = item
    quantity = quantity
    price = get_price(item)
    locked_price = price
    total_price = quantity * price
    check = check_if_item_exists(item)
    # if check == 1:
    #     update_the_order(order_id,quantity,total_price)
    # else:
    order_id = order_id
    add_to_customer_items_table(order_id,item,quantity,locked_price,total_price)

#-------------------------------------------UPDATE DATA IN TABLES------------------------------------------
def remove_from_inventory(quantity,item):
    quantity = quantity
    item = item
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "UPDATE books SET book_quantity = (book_quantity - %s) WHERE book_name = %s"
    val = (quantity,item)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

def add_to_inventory(item,quantity):
    quantity = quantity
    item = item
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "UPDATE books SET book_quantity = (book_quantity + %s) WHERE book_name = %s"
    val = (quantity,item)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

def delete_incomplete_order():
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "DELETE FROM orders ORDER BY order_id desc limit 1"
    cursor.execute(sql)
    close_connection_and_cursor(connection,cursor)

# def add_courier_to_complete_order(order_id,customer_id,courier_id):
#     connection = establish_conection()
#     cursor = connection.cursor()
#     sql = "INSERT INTO orders (order_id,customer_id,courier_id) VALUES (%s,%s,%s)"
#     val = (order_id,customer_id,courier_id)
#     cursor.execute(sql,val)
#     close_connection_and_cursor(connection,cursor)



#----------------------------------------------CHECK VALID-------------------------------------------------
def check_valid_item(item):
    connection = establish_conection()
    cursor = connection.cursor()
    valid_item = item
    sql = """SELECT IF( EXISTS(
             SELECT book_name
             FROM books
             WHERE book_name = %s), 1, 0)"""
    val = (valid_item)
    cursor.execute(sql,val)
    result = cursor.fetchone()
    close_connection_and_cursor(connection,cursor)
    return result[0]

def check_stock_levels(item,quantity):
    connection = establish_conection()
    cursor = connection.cursor()
    valid_item = item
    valid_quantity = quantity
    sql = "SELECT book_quantity FROM books WHERE book_name = %s"
    val = (valid_item)
    cursor.execute(sql,val)
    result = cursor.fetchone()
    close_connection_and_cursor(connection,cursor)
    if result[0] > valid_quantity:
        print("This is in stock")
        return True
    else:
        a = result[0]
        print(f"There is not enough stock. Maximum available is {a}")



#-----------------------------------------TAKE ORDER--------------------------------------------------------
def stop_order():
    stop_taking_items = input("Complete order [y/n]: ")
    if stop_taking_items =="y":
        return True
    else:
        return False

def take_customer_items_for_order(order_id):
    while True:
        item = input("Enter a book: ")
        check_valid = check_valid_item(item)
        if check_valid == 1:
            quantity = int(input("Enter a quantity: "))
            availablity = check_stock_levels(item,quantity)
            if availablity == True:
                assemble_customer_items(order_id,item,quantity)
                remove_from_inventory(quantity,item)
                result = stop_order()
                if result == True:
                    break
                else: 
                    continue
        else:
            print("That is an invalid book")
            result = stop_order()
            if result == True:
                break
            else: 
                continue


#---------------------------------UPDATE ORDER------------------------------------------------------------
def delete_previous_records(order_id):
    connection = establish_conection()
    cursor = connection.cursor()
    order = order_id
    sql = "DELETE FROM customer_order WHERE order_id = %s"
    val = (order)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)


def get_locked_in_price(order,name):
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "SELECT locked_price FROM customer_order WHERE order_id = %s AND book_name = %s"
    val = (order,name)
    cursor.execute(sql,val)
    result = cursor.fetchone()
    close_connection_and_cursor(connection,cursor)
    return result

def add_updated_customer_items(order_id,k,v,fixed_price):
    order = order_id
    name = k
    quantity = v
    price = fixed_price
    total_price = price * quantity
    connection = establish_conection()
    cursor = connection.cursor()
    order = order_id
    sql = "INSERT INTO customer_order (order_id,book_name,book_quantity,locked_price,total_price) VALUES (%s,%s,%s,%s,%s)"
    val = (order,name,quantity,price,total_price)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)


def print_order(my_dict):
    t = PrettyTable(['Book Name', 'Quantity'])
    for x,y in my_dict.items():
        t.add_row([x,y])
    print(t)

def items_to_dict(items,order_id,locked_prices):
    my_prices = dict()
    for x in locked_prices:
        my_prices[x[0]] = x[1]
    print(my_prices)
    my_dict = dict()
    for x in items:
        my_dict[x[0]] = x[1]
    print("This is your order")
    print_order(my_dict)
    for k,v in my_dict.items():
        fixed_price = my_prices.get(k)
        print(f"Would you like to update the quantity of {k} priced at £{fixed_price}")
        user_choice = input("Enter y/n: ")
        if user_choice == "y":
            item = k
            quantity = int(v)
            v = int(input("Enter the value: "))
            print(item,quantity)
            print(k,v)
            add_to_inventory(item,quantity)
            add_updated_customer_items(order_id,k,v,fixed_price)
            remove_from_inventory(v,k)
        else:
            item = k
            v = int(v)
            quantity = v
            add_to_inventory(item,quantity)
            add_updated_customer_items(order_id,k,v)
            remove_from_inventory(quantity,item)

def check_order_complete(order_id):
    connection = establish_conection()
    cursor = connection.cursor()
    order = order_id
    sql = "SELECT final_price FROM orders WHERE order_id = %s"
    val = (order)
    cursor.execute(sql,val)
    result = cursor.fetchone()
    close_connection_and_cursor(connection,cursor)
    return result[0]

def update_order():
    order_id = int(input("Enter an order_id: "))
    value = check_order_complete(order_id)
    if value > 0:
        print("This order is complete and can't be changed")
    else:
        items = get_all_order_items(order_id)
        locked_prices = get_all_order_prices(order_id)
        delete_previous_records(order_id)
        items_to_dict(items,order_id,locked_prices)

#---------------------------------MAKE NEW ORDER------------------------------------------------------------------------
def make_new_order():
    name = input("Enter the customers name: ")
    phone = input("Enter the customers phone: ")
    valid_customer = check_customer_exists(name,phone)
    print(valid_customer)
    if valid_customer == 0:
        delete_incomplete_order()
        print("This customer does not exist")
        make_new_order()
    else:
        customer_id = get_customer_id(name,phone)
        courier_id = get_random_courier()
        order_id = create_order(customer_id, courier_id)
        take_customer_items_for_order(order_id)

#-------------------------------COMPLETE ORDER---------------------------------------------------------------
def calculate_absolute_total(order_id):
    connection = establish_conection()
    cursor = connection.cursor()
    order = order_id
    sql = "SELECT SUM(total_price) FROM customer_order WHERE order_id = %s"
    val = (order)
    cursor.execute(sql,val)
    result = cursor.fetchone()
    close_connection_and_cursor(connection,cursor)
    return result[0]

def complete_order_in_table(a,order_id):
    price = a
    order = order_id
    connection = establish_conection()
    cursor = connection.cursor()
    sql = "UPDATE orders SET final_price = %s WHERE order_id = %s"
    val = (price,order)
    cursor.execute(sql,val)
    sql = "UPDATE orders SET order_status = %s WHERE order_id = %s"
    val = ('Completed',order)
    cursor.execute(sql,val)
    close_connection_and_cursor(connection,cursor)

def complete_order():
    order_id = int(input("Enter an order id: "))
    a = calculate_absolute_total(order_id)
    complete_order_in_table(a,order_id)
    
#-------------------------------VIEW ALL ORDER----------------------------------
def print_all_orders(result):
    t = PrettyTable(['Order ID', 'Customer Name', 'Courier Name', 'Order Total', 'Order Status'])
    for x in result:
        t.add_row([x[0],x[1],x[2],x[3],x[4]])
    print(t)

def view_all_orders():
    connection = establish_conection()
    cursor = connection.cursor()
    sql = """SELECT orders.order_id, customers.customer_name, couriers.courier_name, orders.final_price, orders.order_status
    FROM orders
    LEFT JOIN customers ON customers.customer_id = orders.customer_id 
    LEFT JOIN couriers ON couriers.courier_id = orders.courier_id
    ORDER BY orders.order_status
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    print_all_orders(result)
    close_connection_and_cursor(connection,cursor)
 
take_order_menu()