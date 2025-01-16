# frequecny in the list can be found in two way using inbuild function or leaveraging the power of dictionary 

def frequency_count(lst):
    # create an empty dictionary to store the frequency count
    frequency = {}

    # iterate through the list 
    for num in lst:
        # if the number is present in the dictionary then increase the frequency by 1
        if num in frequency:
            frequency[num] += 1
        # if the number is not in the dictionary then initialize its count to 1
        else:
            frequency[num] = 1

    # iterating to the dictionary to count the frequency
    for key in frequency:
        print(f"'{key}' - '{frequency[key]}'")

numbers = [1, 2, 2, 3, 1, 4, 2, 5, 3, 1]
frequency_count(numbers)



