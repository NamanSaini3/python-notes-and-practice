#  Number Sign Checker Ask the user to enter a number. Print whether it is Positive, Negative, or Zero.
#  Driving License Eligibility Ask the user's age. If age is 18 or above, print "You can apply for a license". Otherwise print "Too young to drive".

userAge = 18

if userAge >= 18:
    print("You can apply for a license")

else:
    print("Too young to drive")
    


# Even or Odd Ask the user to enter a number. Print whether it is Even or Odd.

number = 89

if number % 2 == 0:   # ✅ Check if remainder is 0
    print("Even Number")
else:
    print("Odd Number")

# Temperature Feeling Ask the user for the temperature
#(in °C).Below 10 → "It's cold", 10 to 25 → "It's pleasant", Above 25 → "It's hot"


userTemperature = 2

if userTemperature < 10:        # Below 10 → Cold
    print("It's cold")
elif userTemperature <= 25:     # 10 to 25 → Pleasant
    print("It's pleasant")
else:                           # Above 25 → Hot
    print("It's hot")





# Shop Discount Calculator Ask the user for the total bill amount.
# Above ₹1000 → 20% discount, Above ₹500 → 10% discount, Otherwise → No discount

# Login System Set a username and password in your code. Ask the user to enter both.
#  If both match, print "Login Successful", else print "Wrong credentials".

username = "admin"
password = "1238"

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong credentials")



# Electricity Bill Calculator Ask for units consumed.
# Up to 100 units → ₹6 per unit
# 101–200 units → ₹8 per unit
# Above 200 units → ₹10 per unit

Units = 780

if Units <= 100:
    Bill = Units * 6
elif Units <= 200:
    Bill = Units * 8
else:
    Bill =  Units * 10 

print("Total bill is" , Bill)



# BMI Calculator Ask for weight (kg) and height (m). Calculate BMI = weight / height².
# Below 18.5 → "Underweight", 18.5 to 24.9 → "Normal", 25 to 29.9 → "Overweight", 30 or above → "Obese"

