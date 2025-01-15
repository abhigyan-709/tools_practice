def fibo(n):
    fib_sequence = [0, 1]
    for i in range(2, n):

        next_number = fib_sequence[i - 1] + fib_sequence[i - 2] 
        fib_sequence.append(next_number)
    return fib_sequence

def main():
    n = int(input("Enter the maximum limit of sequence: "))
    print(fibo(n))
    

if __name__ == "__main__":
    main()


# def fibonacci(n):
#     fib_sequence = [0, 1]
#     for i in range(2, n):
#         next_number = fib_sequence[i-1] + fib_sequence[i-2]
#         fib_sequence.append(next_number)
#     return fib_sequence

# # Example: Generate Fibonacci series up to the 10th number
# n = 10
# print(fibonacci(n))


