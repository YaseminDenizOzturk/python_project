('''                __,__
        .--.  .-"     "-.  .--.
       / .. \/  .-. .-.  \/ .. \
      | |  '|  /   Y   \  |'  | |
      | \   \  \ 0 | 0 /  /   / |
       \ '- ,\.-"`` ``"-./, -' /
        `'-' /_   ^ ^   _\ '-'`
        .--'|  \._   _./  |'--. 
      /`    \   \ `~` /   /    `\
     /       '._ '---' _.'       \
    /           '~---~'   |       \
   /        _.             \       \
  /   .'-./`/        .'~'-.|\       \
 /   /    `\:       /      `\'.      \
/   |       ;      |         '.`;    /
\   \       ;      \           \/   /
 '.  \      ;       \       \   `  /
   '._'.     \       '.      |   ;/_
jgs  /__>     '.       \_ _ _/   ,  '--.
   .'   '.   .-~~~~~-. /     |--'`~~-.  \
  // / .---'/  .-~~-._/ / / /---..__.'  /
 ((_(_/    /  /      (_(_(_(---.__    .'
           | |     _              `~~`
           | |     \'.
            \ '....' |
             '.,___.'
''')

print("Can you find the banana? ")
print("Follow the steps")

choice1 = input("Do you want to take the right or the left road? L or R ").lower()

if choice1 == "left":
    choice2 = input("There are rabbits in front of you. Would you like to feed them? Y or N")
else:
    choice3 = input("Do you want to go for a boat ride? Y or N ")

if choice2 == "Y":
    choice4 = input("follow the rabbits(1)  or swimming across(2) ?  ")
else:
    print("Game Over!")

if choice3 == "Y":
    print("Game over")

else: 
    choice5 = input("tree-lined road(1) or stony road(2) ? " )

if choice5 == "1":
    print("GREAT GOAL ACHIEVED!")
else:
    print("Game over")

if choice4 == "1":
    print("GREAT GOAL ACHIEVED!")
else:
    print("Game over")








