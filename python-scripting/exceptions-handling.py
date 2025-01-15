# exception handling with multiple except block
try:

    number = int(input("Enter the integer: "))
    divisor = int(input("Enter the divisior: "))
    print(f"'{number}' divided by '{divisor}' is '{number/divisor}'")

except ValueError:
    print("Enter a valid number")

except ZeroDivisionError:
    print("Number can not be divided by zero")

except Exception as e:
    print(f"Unexpected error occured '{e}'")

# exception handling with else block:
try: 
    number = int(input("Enter a new number: "))

except ValueError:
    print("Integer is not given as input")

else:
    print(f"You have entered '{number}'")

# using finally clause, this will execute at any how, whether the exception cause or not 

try: 
    number2 = int(input("Enter a new number: "))

except ValueError:
    print("Integer is not given as input")

else:
    print(f"You have entered '{number2}'")

finally:
    print("Executed the finally at any how.")



