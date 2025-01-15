# method 1 using split and reversed function

my_string = "This is my list to be reversed"
list1 = my_string.split()
print(list1)
list2 = list(reversed(list1))
list3 = ' '.join(list2)
print(list3)

# method 2 using the other method
my_string2 = "This is my second string"
my_string2 = my_string2.split()

print(my_string2)
reversed_string = my_string2[::-1]
reversed_string = ' '.join(reversed_string)

print(reversed_string)

# method 3 using the loop, without using the slicing and reversed


def reverse_string(your_string):
    result = ""
    for char in your_string:
        result = char + result
    
    return result

def main():
    your_string = str(input("Enter your string to get reversed: "))
    print(reverse_string(your_string))


if __name__ == "__main__":
    main()
    


