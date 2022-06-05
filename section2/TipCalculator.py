bill_amount = float(input("Enter total bill amount:"));
tip_percentage = int(input("Enter tip '%' as 10,12,15:"));
tip_amount = (bill_amount/100)*tip_percentage;
total_bill_amount = bill_amount+tip_amount;
members = int(input("Enter total members to divide the bill"));
individual_amount = total_bill_amount/members;

print(f"Each member has to pay {individual_amount} including tip");