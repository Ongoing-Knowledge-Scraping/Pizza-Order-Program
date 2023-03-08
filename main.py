# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries! \n")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 3
    elif size == "M":
        bill += 4
    else:
        bill += 5

if extra_cheese == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    else:
        bill += 4

print(f"Your total bill is ${bill}")
