# 0, 1, and negative numbers can not be prime number 
# number divisible by 1 and itself is known as prime number 

def is_prime(n):
    if n <= 1:
        print("Number can not be 1, 0 or negative to check prime.")

    elif n <= 3:
        print(f"The number '{n}' is prime")

    elif n % 2 == 0 or n % 3 == 0:
        print(f"Number '{n}' is not a prime number.")

    else:
        i = 5 
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        print("The number is prime number.")
    
def main():
    try:
        n = int(input("Enter the number you want to check for the prime: "))
        is_prime(n)
    except ValueError:
        print("You have not enteres the correct integer.")
    finally:
        print("That's all for today, thanks for using this function.")


if __name__=="__main__":
    main()


