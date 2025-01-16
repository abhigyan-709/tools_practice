import math

options = {
    1 : "Add",
    2 : "Subtract",
    3 : "Multiply",
    4 : "Divide",
    5 : "Percentage",
    6 : "Square Root",
    7 : "Power"
}

def addition():
    addition_number = int(input("How many numbers to add: "))
    add_list = []

    for i in range(addition_number):
        number = int(input("Enter the number : "))
        add_list.append(number)

    print(sum(add_list))

def subtract():
    a = int(input("Value of a: "))
    b = int(input("Value of b: "))

    print(a - b)

def multiply():
    pass
def divide():
    pass
def percentage():
    pass
def square_root():
    pass
def power():
    pass



def main():
    for key in options:
        print(f"{key} - {options[key]}")

    try:
        option = int(input("Choose the option to perform calculation: "))
        print(f"You have chosen {option} to {options[option]}")
    except ValueError:
        print("Please type correct input")

    if option == 1:
        addition()

    elif option == 2:
        subtract()

if __name__ == "__main__":
    main()