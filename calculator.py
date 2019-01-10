"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

import arithmetic

def math_operations(input_list):

    
    input_length = len(input_list)
    
    operator = input_list[0]

    if input_length == 2:

        num1 = float(input_list[1])

    elif input_length == 3:
        num1 = float(input_list[1])
        num2 = float(input_list[2])
    
    if operator == "+":
        return arithmetic.add(num1, num2)
    
    elif operator == "-":
        return arithmetic.subtract(num1, num2)
        
    elif operator == "*":
        return arithmetic.multiply(num1, num2)

    elif operator == "/":
        return arithmetic.divide(num1, num2)

    elif operator == "square":
        return arithmetic.square(num1)

    elif operator == "cube":
        return arithmetic.cube(num1)

    elif operator == "pow":
        return arithmetic.power(num1, num2)

    elif operator == "mod":
        return arithmetic.mod(num1, num2)

def prompt_user_input():
    # prompt user
    # if no input given, prompt again

    while True:
        
        input_string = input("> ")
        input_list = input_string.split(" ")
        
        
        if input_list[0] != "+" and input_list[0] != "-" and input_list[0] != "*" and input_list[0] != "/" and input_list[0] != "square" and input_list[0] != "cube" and input_list[0] != "pow" and input_list[0] != "mod" and input_list[0] != "q":
            print("Entry not valid, enter valid terms.")
            continue
        elif input_string != "q":
            print(math_operations(input_list))
            continue
        else:
            print("You've quit the calculator. Goodbye.")
            break        

prompt_user_input()