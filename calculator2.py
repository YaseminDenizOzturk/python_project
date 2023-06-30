calc = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''

print(calc)

def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2


operations = {
    "+": add,
    "-":subtract,
    "*":multiply,
    "/":divide
}


first_number = float(input("What is the first number: "))
for operator in operations:
    print(operator)
should_continue = True


# while True 
while should_continue:
    entered_operator = input("Pick an operation: ")
    second_number = float(input("What is the second number: "))
    calculation_function = operations[entered_operator]
    answer = calculation_function(first_number , second_number)

    print(f"{first_number} {entered_operator} { second_number} = {answer}")

    
    if input(f"Type 'Y' to continue calculating with {answer} , or type 'N' to exit: ").lower() == "y":
        first_number = answer

    else:
        print("process terminated...")
        should_continue = False


