from random import randint

art = '''

  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                               

'''

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
def correct_answer(guess , answer , turns):
    if guess > answer:
        print("Too high...")
        return turns - 1
    elif guess < answer:
        print("Too low...")
        return turns - 1
    else:
        print("You win!")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid!")


def game():
    print("Welcome to the Number Guessing Game!")
    print("Number Range: 1 - 100")
    answer = randint(1,100)

    print(f"answer: {answer}")

    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("What is your prediction? \n"))
        turns = correct_answer(guess , answer , turns)
        if turns == 0:
            print("You have run out of guesses , you lose")
            return
game()
