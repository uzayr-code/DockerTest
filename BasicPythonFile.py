# Functions

def add_numbers(num1, num2):
    """This function takes two numbers as input and returns their sum."""
    return num1 + num2

def multiply_numbers(num1, num2):
    """This function takes two numbers as input and returns their product."""
    return num1 * num2

def divide_numbers(num1, num2):
    """Return the result of dividing num1 by num2.

    Print "babaooey" when the result equals 4.
    """
    result = num1 / num2
    if result == 4:
        print("babaooey")
    return result

def display_outputs(outputs):
    """Print each calculator result stored in the output list."""
    for output in outputs:
        print(output)


# Main program

def main(outputs=None):
    if outputs is None:
        outputs = []

    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    
    choice = input("Do you want to add or multiply the numbers? (add/multiply): ").strip().lower()
    
    if choice == "add":
        result = add_numbers(number1, number2)
        outputs.append(f"The sum of {number1} + {number2} is: {result}")
    elif choice == "multiply":
        result = multiply_numbers(number1, number2)
        outputs.append(f"The product of {number1} * {number2} is: {result}")

    continue_choice = input("Do you want to perform another operation? (yes/no): ").strip().lower()

    if continue_choice == "yes":
        main(outputs)
    else:
        display_outputs(outputs)
        print("Thank you for using the calculator!")
        
# Run the program when this file is executed directly.
if __name__ == "__main__":
    main()
