# calculate the factorial of the number

# method 1
import math 

def factorial_calculate(n):
    return math.factorial(n)

def main():
    try:
        n = int(input("Enter the number to find the factorial: "))
        print(factorial_calculate(n))

    except ValueError:
        print("You did not entered the correct integer.")

if __name__=="__main__":
    main()

# method 2 by using loop

def factorial2(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result
n = int(input("Enter the number to calculate the factorial: "))
print(factorial2(n))


# method 3 using recursion 

def factorial3(n):
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial3(n - 1)
    
print(factorial3(5))
        