import random

def select_courier(courier):
    with open("couriers.txt", "r") as f:
         courier_list = [line.strip('\n') for line in open("couriers.txt")]
         random_couriers = []
         for i in range(4):
             random_courier = random.choice(courier_list)
             if random_courier in random_couriers:
                 random_courier = random.choice(courier_list)
                 random_couriers.append(random_courier)
             else:
                 random_couriers.append(random_courier)

    print("Select a courier from the list below")
    for i in range(4):
        print(f"{i} : {random_couriers[i]} is {round(random.uniform(0, 1),2)} miles away")
    
    usr_input = int(input("Enter a number: "))
    match usr_input:
        case 0:
            courier = random_couriers[0]
        case 1:
            courier = random_couriers[1]
        case 2:
            courier = random_couriers[2]
        case 3:
            courier = random_couriers[3]
    return courier
    





