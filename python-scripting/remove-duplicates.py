# removing duplicates from the list 
# method 1
list1 = [1, 2, 4, 5, 3, 2, 1]

print(list(set(list1)))

# the above uses the set method and returns the list in the ascending order

# method 2
# this uses the looping techiniques and returns the list in non-sorted order
list2 = [1, 2, 4, 5, 1, 2, 4, 5, 6, 3]

non_init = []

for num in list2:
    if num not in non_init:
        non_init.append(num)

print(non_init)