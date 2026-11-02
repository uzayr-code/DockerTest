# ToDo Create a basic Python file with a simple function that takes two numbers as input and returns their sum.
def add_numbers(num1, num2):
    """This function takes two numbers as input and returns their sum."""
    return num1 + num2

def multiply_numbers(num1, num2):
    """This function takes two numbers as input and returns their product."""
    return num1 * num2


def main():
    # Example usage of the add_numbers function
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    
    choice = input("Do you want to add or multiply the numbers? (add/multiply): ").strip().lower()
    
    if choice == "add":
        result = add_numbers(number1, number2)
        print(f"The sum of {number1} + {number2} is: {result}")
    elif choice == "multiply":
        result = multiply_numbers(number1, number2)
        print(f"The product of {number1} * {number2} is: {result}")

    continue_choice = input("Do you want to perform another operation? (yes/no): ").strip().lower()

    if continue_choice == "yes":
        main()  # Call main again for another operation
    else:
        print("Thank you for using the calculator ?")
        
# When you run a pyhton file directly, its __name__ variable is set to "__main__". 
if __name__ == "__main__":
    main()