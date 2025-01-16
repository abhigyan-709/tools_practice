# sorting the given list by the methods

# inbuilt sorted function:

# type 1 remove the duplicates and sort in both order


list1 = [1, 2, 4, 5, 6, 7, 2, 3, 2, 1, 4]
sorted_list = list(set(list1))

print(f"Sorted list in Decending Order '{sorted_list[::-1]}'")
print(f"Sorted list in Ascending Order '{sorted_list}'")

# type 2 remove duplicates and then sort without sets & sorted method

list2 = [1, 2, 2, 3, 2, 1, 2, 4, 5, 6, 4, 5]
sort_list = []

# remove duplicates first
for num in list2:
    if num not in sort_list:
        sort_list.append(num)

print(f"Refined list '{sort_list}'")
# sort the element in the newly generated list 
# for sort list or list having less length 

def bubble_sort(lst):
    n = len(lst)

    # traverse thorough the list 
    
    for i in range(n):
        # last i elements is already sorted so not considering them 
        for j in range(0, n-i-1):
            # comparing the elements and swapping them if found greater than second element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

list3 = [1, 2, 2, 3, 2, 1, 2, 4, 5, 6, 4, 5]
bubble_sort(list3)
print(list3)

def bubble_sort(lst):
    n = len(lst)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already sorted, so we can skip them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# Example usage
list1 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(list1)
print("Sorted list:", list1)




        