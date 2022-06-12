height =int(input("Enter your height(cm):"));
if height>=120:
    age = int(input("Enter your age:"));
    if age<=18:
        print("Ticket price is 10$");
    elif age<=30:
        print("Ticket price is 15$");
    elif age>30:
        print("Ticcket price is 20$");
else:
    print("Sorry! you are not eligible for roller coaster as your height is less")
