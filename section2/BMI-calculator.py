# General formal for BMI calculator: weight(kg)/height*2(m)



weight = int(input("Enter your weight in KG: \n"))
height = int(input("Enter your height in CM: \n"))

BMI = weight/(height*2/100);
if BMI>30:
    print(f"You are obese! as your BMI is: {int(BMI)}");
    
elif BMI>25 and BMI<=30:
    print(f"You are overweight as your BMI is: {int(BMI)}");
elif BMI>=18.5 and BMI<=25:
    print(f"You are normal as your BMI is: {int(BMI)}");
else:
    print(f"You are underweight as your BMI is: {int(BMI)}");