age = input("What is your current age : ")
age_as_int = int(age)

years_left = 90-age_as_int
days_left = years_left * 365
month_left = years_left * 12
weeks_left = years_left * 52

print(f"You have {days_left} days left,\nYou have {month_left} months left,\nYou have {weeks_left} weeks left")


