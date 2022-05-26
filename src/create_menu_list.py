
def add_from_file(customer_list):
    textfile = open("customer_list.txt", "w")
    for item in customer_list:
        textfile.write(item + "\n")
    textfile.close()

def create_list():
    items = [word.strip('\n') for word in open("items.txt", 'r').readlines()]
    print(*items, sep='\n')
    customer_list = []

    while True:
        user_menu_input = input("Enter an item or press [x] to exit: ")

        if user_menu_input in items:
            customer_list.append(user_menu_input)
            print(*customer_list, sep='\n')
        elif (user_menu_input == "x"):
            print(*customer_list, sep='\n')
            break
        else:
            break

    add_from_file(customer_list)