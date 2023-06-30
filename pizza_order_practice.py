print("Welcome to Jasmine Pizza House")
size = input("What size pizza do you want? S , M or L ?")
pizza_types = input("Which type of pizza do you want? Margarita(1) , Marinara(2) , Supreme(3) , Pepperoni(4) , Gennaro(5) , Supreme Stuffed(6) , Mixed(7) ")
add_mushrooms = input("Do you want mushrooms on your pizza? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
add_green_peppers = input("Do you want green peppers? Y or N ")
add_black_olives = input("Do you want black olives? Y or N ")
add_mexican_chili_pepper = input("Do you want Mexican chili pepper? Y or N ")


bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("invalid!")

if pizza_types == "1":
    bill += 2
elif pizza_types == "2":
    bill += 3
if pizza_types == "3":
    bill += 3
if pizza_types == "4":
    bill += 3
if pizza_types == "5":
    bill += 4
if pizza_types == "6":
    bill += 4
if pizza_types == "7":
    bill += 4

if add_mushrooms == "Y":
    if size == "S":
         bill += 2
    elif size == "M":
        bill += 3
    else:
         bill += 4

if extra_cheese == "Y":
    if size == "S":
        bill += 1
    elif size == "M":
        bill += 2
    else:
        bill += 3

if add_green_peppers == "Y":
    if size == "S":
        bill += 1
    elif size == "M":
        bill += 2
    else:
        bill += 3

if add_black_olives == "Y":
    if size == "S":
        bill += 1
    elif size == "M":
        bill += 2
    else:
        bill += 3

if add_mexican_chili_pepper == "Y":
    if size == "S":
        bill += 1
    elif size == "M":
        bill += 2
    else:
        bill += 3

        
print(f"Your final bill is ${bill}")

