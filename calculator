# TASK 1

# CALCULATOR APP

# ● Design a simple calculator with basic arithmetic operations.
# ● Prompt the user to input two numbers and an operation choice.
# ● Perform the calculation and display the result.

def calculator():

    # Taking two numbers as a user input
    num1 = int(input("Enter the number 1: "))
    num2 = int(input("Enter the number 2: "))

    # Displaying operation to user
    print('''
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

    # Taking operation as user's choice
    operation = input("Enter your desired operation: ")

    # Using conditional statements to verify the result
    if (operation == '+'):
        answer = num1 + num2

    elif (operation == '-'):
        answer = num1 - num2

    elif (operation == '*'):
        answer = num1 * num2

    elif (operation == '/'):
        # Validating case of division by ZERO
        if (num2 == 0):
            answer = print("Math Error! Zero Division Error")
        else:
            answer = num1 / num2
    else:
        print("Please enter valid operation")

    # Displaying result 
    print(f"Your answer is: {answer}")

calculator()                                
