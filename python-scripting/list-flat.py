# faltting the nested list in two ways: 
# this is the recursive method where the function flatten_list() is getting called each time, while tracesring throigh the nested list
# isinstance is used to check the type of the object at the runtime

# method 1 - recursion
def flatten_list(nested_list):
    flatted_list = []

    for element in nested_list:
        if isinstance(element, list):
            flatted_list.extend(flatten_list(element))

        else:
            flatted_list.append(element)

    return flatted_list

nested_list = [1, 2, [1, 2, 4], 4, 5, 6, [2, 3]]
flatted = flatten_list(nested_list)

print(flatted)

