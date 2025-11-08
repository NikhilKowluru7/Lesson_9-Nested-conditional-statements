medicalcause = input("Do you have a medical reason?(yes/no): ")
if medicalcause.lower() == "yes":
    print("You are eligible for the examinations!")
else:
    attendence = float(input("Enter your attendace percentage: "))
    if attendence >70:
        print("You are eligible for the examinations!")
    else:
        print("You are not eligible for the examinations!")