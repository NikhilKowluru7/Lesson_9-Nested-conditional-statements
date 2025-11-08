print("Welcome to Rent a Ride!")
choice1= int(input("Choose a vehicle\n 1.Car\n 2.Motorbike\n Pick either 1 or 2:  "))
if choice1==1:
    choice2 = int(input("Choose a car\n 1. Lamborghini\n 2. Bugatti\n Pick either 1 or 2: "))
    if choice2 ==1:
        print("Your Lamborghini is set to go!")
    elif choice2 ==2:
        print("Your Bugatti is set to go!")
    else:
        print("Wrong choice of car!")
elif choice1 ==2:
    choice2 = int(input("Choose a motorbike\n 1. Honda\n 2. R15\n Pick either 1 or 2: "))
    if choice2 ==1:
        print("Your Honda is set to go!")
    elif choice2 ==2:
        print("Your R15 is set to go!")
    else:
        print("Wrong choice of motorbike!")
else:
    print("Wrong choice of vehicle!")