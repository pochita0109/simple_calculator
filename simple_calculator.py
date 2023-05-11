# Kenneth John Costa
# Assignment 5
# Simple Calculator

print("\033[93m-" * 80)
print("Simple Calculator".center(80))
print("\033[93m-" * 80)

# Show the operation that is available on simple calculator
print("\033[0mADDITION: \033[94m1".center(81))
print("\033[0mSUBTRACTION: \033[91m2".center(85))
print("\033[0mMULTIPLICATION: \033[92m3".center(87))
print("\033[0mDIVISION: \033[95m4".center(81))

while True:
        try:
# Ask the user to enter the first number
            first_number = float(input("Please enter the first number: "))
# Ask the user to enter the second number
            second_number = float(input("Please enter the second number: "))
# Ask the user about the operation they want to use (1-4)
            operation = int(input("\033[94mPlease enter the operation that you want to use (1,2,3,4): "))
    # If the user entered invalid character:
        except ValueError:
            print("Error! the value that you have entered is invalid".upper())
            continue

# If addition (1)
    # Print the result
# If subtraction (2)
    # Print the result 
# If multiplication (3)
    # Print the result
# if division (4)
    # Print the result
    # If the user entered zero as a divisor:

# Ask the user if they want to continue on using mini calculator (Y/N)
# If Y:
# If N:
# If the user entered other characters than Y or N:
    