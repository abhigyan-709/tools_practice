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
