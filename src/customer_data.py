
# Takes input from user and saves into a file to be used later

def customer_data():
    with open("name.txt", "w") as file:
        file.write(input("Enter a name: "))
    
    with open("address.txt", "w") as file:
        file.write(input("Enter an address: ")) 

    with open("phone.txt", "w")as file:
        file.write(input("Enter a phone number: "))


        
