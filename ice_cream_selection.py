print("Welcome!")

choice = int(input("What kind of ice cream would you like? with banana(1), with strawberries(2) or with chocolate(3)? "))
scoops = int(input("How many scoops of ice cream do you want? 1 , 2 or 3 ?"))


if choice == 1:
    if scoops == 1:
        print("you will pay 3$")
    elif scoops == 2:
        print("you will pay 6$")
    elif scoops == 3:
        print("you will pay 9$")
    else:
        print("invalid!")
elif choice == 2:
    if scoops == 1:
        print("you will pay 3$")
    elif scoops == 2:
        print("you will pay 6$")
    elif scoops == 3:
        print("you will pay 9$")
    else:
        print("invalid!")
elif choice == 3:
    if scoops == 1:
        print("you will pay 3$")
    elif scoops == 2:
        print("you will pay 6$")
    elif scoops == 3:
        print("you will pay 9$")
    else:
        print("invalid!")
else: 
    print("invalid!")
wants_nut = input("Do you want nuts? 'Y' OR 'N' ")
if wants_nut == "Y":
    print(f"you have to pay extra 2$ ")
else:
    print("Have a nice day")

