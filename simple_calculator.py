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
        if operation == 1:
            while True:
                    # Print the result
                    sum = first_number + second_number
                    print(f"The sum is {sum} \n")
                    break
         
        # If subtraction (2)
        elif operation == 2:
            while True:
                    # Print the result
                    difference = first_number - second_number
                    print(f"The difference is {difference} \n")
                    break
             
        # If multiplication (3)
        elif operation == 3:
             while True:
                    # Print the result
                    product = first_number * second_number
                    print(f"The product is {product} \n")
                    break
             
        # if division (4)
        elif operation == 4:
             while True:
                    try:
                        # Print the result
                        quotient = first_number / second_number
                        print(f"The quotient is {quotient} \n")
                        break
                        # If the user entered zero as a divisor:
                    except ZeroDivisionError:
                        print("ERROR! YOU HAVE ZERO DIVISOR, PLEASE TRY AGAIN \n")
                        break
        else:
            print("Error! the value that you have entered is invalid".upper())

        while True:  
            # Ask the user if they want to continue on using mini calculator (Y/N)
            answer = input("Type Y if you want to continue on using the simple calculator or N if not: ")
# If Y:
# If N:
# If the user entered other characters than Y or N:
    