# General formal for BMI calculator: weight(kg)/height*2(m)

weight = int(input("Enter your weight in KG: \n"))
height = float(input("Enter your height in M: \n"))

BMI = weight/(height**2)

print(f"Your BMI is : {int(BMI)}")