# method 1 to check the key

my_dict = {
    "name" : "abhigyan",
    "id" : 709
}

if "name" in my_dict:
    print(f"The key name is present in the dictionary")

else:
    raise ValueError("Specified key not found")


my_dict2 = {
    "name" : "abhigyan",
    "id" : 709,
}

if 'name' in my_dict2.keys():
    print("Specified key exists in the dictionary.")

