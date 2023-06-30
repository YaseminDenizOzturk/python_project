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

first_number = int(input("What is the first number: "))
second_number = int(input("What is the second number: "))

for operator in operations:
    print(operator)

entered_operator = input("Pick an operator from the line above: ")
calculation_function = operations[entered_operator]
answer1 = calculation_function(first_number , second_number)

print(f"{first_number} {entered_operator} {second_number} = {answer1}")

entered_operator = input("Pick another operation: ")
third_number = int(input("What is the next number: "))

calculation_function = operations[entered_operator]

answer2 = calculation_function(calculation_function(first_number , second_number) , third_number)

print(f"{answer1} {entered_operator} { third_number} = {answer2} ")


