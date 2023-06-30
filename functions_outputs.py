def revised_name(first_name , last_name):
    if first_name == "" or last_name == "":
        return "you didn't provide valid inputs"

    revised_first_name = first_name.title()
    revised_last_name = last_name.title()
    return f"{revised_first_name} {revised_last_name}"

revised_string = revised_name("YaseMİN" , "dENiz")
print(revised_string)

print(revised_name(input("What is your first name? "),input("What is your last name? ")))

