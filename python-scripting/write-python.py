# writing file in the write mode 

file_path = "./python-scripting/newfile.txt"

with open(file_path, 'w') as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")

print(f"Data has been written to {file_path}.")

# writing file in the append mode
# this mode add the line in the file in the last or it creates new line
# this does not overwrites the file 

file_path = "./python-scripting/newfile.txt"
with open(file_path, 'a') as file:
    file.write("This is third line in added in append mode.\n")

print(f"New line has been added in the append mode to the '{file_path}'")

# writing the file in 'x' mode
# it creates new file and raise and error if the file already exists 

file = "xmode_file.txt"

try:
    with open(file, 'x') as newfile:
        newfile.write("New line to the new file.\n")
        newfile.write("Second line to the new file.\n")

except FileExistsError:
    print(f"The file specified with the name '{file} already exists'")