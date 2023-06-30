import random

rock = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''
scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)


'''

game_images = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors. \n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number,you lose!")
else:
    print(game_images[user_choice])

    cmp_choice = random.randint(0,2)
    print(f"computer choose: ")
    print(game_images[cmp_choice])


    if user_choice == 0 and cmp_choice == 2:
        print("User Wins!")
    elif cmp_choice == 0 and user_choice == 2:
        print("Computer Wins!")
    elif cmp_choice > user_choice:
        print("Computer Wins!")
    elif user_choice > cmp_choice:
        print("User Win!")
    elif cmp_choice == user_choice:
        print("It's a draw")
    else:
        print("You entered an invalid character!")

