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

def add():
    pass
def subtract():
    pass
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


    option = int(input("Enter you choice: "))
    if option in options:
        print(f"You have chosen to {option} to {options[option]}")

    


if __name__ == "__main__":
    main()