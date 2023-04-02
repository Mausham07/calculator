"""
Name : Mausham Bista


This is program for a simple calculator which does basic arithmetic
calculations from the number given by users.
"""

# Import math 
import math


# Basic calculator functions
def mb_add(x, y):
    """This function add the value given by user"""
    return x + y

def mb_sub(x, y):
    """This function subtract the value given by user"""
    return x - y

def mb_multiply(x, y):
    """This function multiply the value given by user"""
    return round(x * y, 3)

def mb_divide(x, y):
    """This function divide the value given by user"""
    if y == 0:
        print()
        raise ValueError("Cannot divide by zero!")
    return round(x / y, 3)


# Scientific calculator functions
def mb_squareRoot(x):
    """This function finds the square root of a number"""
    return round(math.sqrt(x), 3)

def mb_exponent(x, y):
    """This function raise a number to a power"""
    return round(x**y, 3)

def mb_sin(x):
    """This function finds the sine of an angle in radians"""
    return round(math.sin(x), 3)

def mb_cos(x):
    """This function finds the cosine of an angle in radians"""
    return round(math.cos(x), 3)

def mb_tan(x):
    """This function finds the tangent of an angle in radians"""
    return round(math.tan(x), 3)

def main ():
    """
    This is a main function of this program which calls other
    functions.
    """
    print("---Welcome to the Python Calculator!---\n")
    print("---Please select an operarion from the following list:")


    while True:
        try:
            # Get user input for the operation to perform
            print("\n1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Square Root")
            print("6. Exponent")
            print("7. Sine")
            print("8. Cosine")
            print("9. Tangent")
            print("10. Quit")
            print()
            mb_choice = input("Enter choice (1-10): ")

            if mb_choice == '10':
                # Quit the program if user chose to exit
                print()
                print("--THANK YOU SO MUCH FOR USING PYTHON CALCULATOR--")
                break
            
            else: 
                # Call the functions to get the value from user
                mb_num1 = mb_get_firstNumber()
                mb_num2 = mb_get_secondNumber()
            
                # Perform the selected operation

                if mb_choice == '1':
                    mb_result = mb_add(mb_num1, mb_num2)
                
                elif mb_choice == '2':
                    mb_result = mb_sub(mb_num1, mb_num2)
                
                elif mb_choice == '3':
                    mb_result = mb_multiply(mb_num1, mb_num2)
                
                elif mb_choice == '4': 
                    mb_result = mb_divide(mb_num1, mb_num2)
                
                elif mb_choice == '5':
                    while True:
                        mb_select = input("Which number you want to perform square root?(first/second): ")
                        if mb_select == 'first':
                            mb_result = mb_squareRoot(mb_num1)
                            break
                        elif mb_select == 'second':
                            mb_result = mb_squareRoot(mb_num2)
                            break
                        else:
                            print()
                            print("---PLEASE ENTER THE VALID ANSWER---\n")
                            print()


                elif mb_choice == '6':
                    mb_result = mb_exponent(mb_num1, mb_num2)

                elif mb_choice == '7':
                    while True:
                        mb_select = input("Which number you want to perform sin calulation?(first/second): ")
                        if mb_select == 'first':
                            mb_result = mb_sin(mb_num1)
                            break
                        elif mb_select == 'second':
                            mb_result = mb_sin(mb_num2)
                            break
                        else:
                            print()
                            print("---PLEASE ENTER THE VALID ANSWER---\n")
                            print()
                   


                elif mb_choice == '8':
                    while True:
                        mb_select = input("Which number you want to perform cos calculations?(first/second): ")
                        if mb_select == 'first':
                            mb_result = mb_cos(mb_num1)
                            break
                        elif mb_select == 'second':
                            mb_result = mb_cos(mb_num2)
                            break
                        else:
                            print()
                            print("---PLEASE ENTER THE VALID ANSWER---\n")
                            print()

                elif mb_choice == '9':
                   while True:
                        mb_select = input("Which number you want to perform tangent calculation?(first/second): ")
                        if mb_select == 'first':
                            mb_result = mb_tan(mb_num1)
                            break
                        elif mb_select == 'second':
                            mb_result = mb_tan(mb_num2)
                            break
                        else:
                            print()
                            print("---PLEASE ENTER THE VALID ANSWER---\n")
                            print()
                
            # Print the result
            print()
            print(f"The desired result is: {mb_result}")
            print()

            # Get user input for whether to continue or not
            mb_choice = input("Do you want to continue? (y/n): ")

            if mb_choice == 'n':
                # Quit the program if the user chose to exit
                break
        
        except ValueError as ve:
            print(f"ValueError occurred: {ve}")
        
        except Exception as e:
            print(f"An error occured: {e}")
            continue

def mb_get_firstNumber():
    # This functions get the first number from user
    num1 = float(input("Enter the first number: "))
    return num1

def mb_get_secondNumber():
    # This functions get the second number from user
    num2 = float(input("Enter the second number: "))
    return num2

if __name__ == "__main__":
    main()