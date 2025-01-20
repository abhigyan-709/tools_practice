import math
from colorama import Fore, Style, init

options = {
    0: "Exit",
    1: "Add",
    2: "Subtract",
    3: "Multiply",
    4: "Divide",
    5: "Percentage",
    6: "Square Root",
    7: "Power",
}


def addition():
    addition_number = int(input(Fore.CYAN + "How many numbers to add: "))
    add_list = []

    for i in range(addition_number):
        number = int(input("Fore.CYAN + Enter the number : "))
        add_list.append(number)

    print(f"Addition of the numbers {add_list} is {sum(add_list)}")


def subtract():
    a = int(input("Value of a: "))
    b = int(input("Value of b: "))

    print(a - b)


def multiply():
    numbers = int(input("How many numbers to multiply: "))
    result = 1
    for _ in range(numbers):
        num = int(input("Enter the number: "))
        result *= num
    print(f"Result: {result}")


def divide():
    a = int(input("Value of a: "))
    b = int(input("Value of b: "))
    if b == 0:
        print("Division by zero is not allowed.")
    else:
        print(f"Result: {a / b}")


def percentage():
    a = float(input("Enter the total: "))
    b = float(input("Enter the value: "))
    print(f"Result: {(b / a) * 100}%")


def square_root():
    a = float(input("Enter the number: "))
    print(f"Result: {math.sqrt(a)}")


def power():
    a = int(input("Base: "))
    b = int(input("Exponent: "))
    print(f"Result: {a ** b}")


def main():
    while True:
        for key in options:
            print(Fore.YELLOW + f"{key} - {options[key]}")

        try:
            option = int(
                input(Fore.CYAN + "Choose the option to perform calculation (press 0 to exit): ")
            )
        except ValueError:
            print(Fore.RED + "Please type correct input")
            continue

        if option == 0:
            print("Exiting the calculator, good bye.")
            break

        if option in options:
            print(f"You have chosen to {options[option]}")

            if option == 1:
                addition()
            elif option == 2:
                subtract()
            elif option == 3:
                multiply()
            elif option == 4:
                divide()
            elif option == 5:
                percentage()
            elif option == 6:
                square_root()
            elif option == 7:
                power()
        else:
            print("invalid input, please choose correct option.")


if __name__ == "__main__":
    main()
