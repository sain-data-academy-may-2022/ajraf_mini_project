import os

# Deletes a file

def delete_order():
    file = (input("Enter an order number: ") +".json")
    if os.path.exists(file):
        os.remove(file)
    else:
        print("The file does not exist")