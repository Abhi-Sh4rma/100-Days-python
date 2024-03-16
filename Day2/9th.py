print("Welcome to the tip calculator.")
Total_bill =float(input("What was the total bill?"))
Tip = int(input("What percent tip would you like to give? 10, 12 or 15?"))
Total_People = int(input("How many people to split the bill?"))
Payable =Tip /100 * Total_bill +Total_bill

new_payble =Payable / Total_People
round(new_payble,2)


print (f"Each person should pay {new_payble}")

