# method 1 without using inbuilt function


list1 = [3, 5, 7, 2, 5]

min_value = list1[0]
max_value = list1[0]

for num in list1:
    if num < min_value:
        min_value = num
    elif num > max_value:
        max_value = num

print(f"Maxmimum value in '{list1}' is '{max_value}'")
print(f"Minimum value in '{list1}' is '{min_value}'")

        
# method 2 by using inbuilt function
list2 = [1,5, 6, 3, 1, 4, 6]
print(f"Minimum value '{min(list2)}'")
print(f"Maxmimum value '{max(list2)}'")

# method 2 using the more optimized way when the list is too large or we are dealing with large dataset 
# single pass: list will done in single pass method in single iteration


def min_max(lst):

    if not lst:
        return None, None # handling the empty list case 
    min_value = max_value = lst[0] # initialize the min and max value at the list at index 0

    for num in lst:
        if num < min_value:
            min_value = num

        elif num > max_value:
            max_value = num


    print(f"The minimum value in the '{lst}' is '{min_value}'")
    print(f"The maximum value in the '{lst}' is '{max_value}'")

my_list = [1,2 , 46, 1, 2, 35, 6, 8, 3, 4]
min_max(my_list)


# method 3 using parallel computing for extremely large datasets
# if we have millions of data set then we can use multithreading and unleash the power of parallel computing
# here we will divide the large data sets in the chunks of the small datasets

from concurrent.futures import ThreadPoolExecutor

def min_max_chunks(chunk):
    pass

