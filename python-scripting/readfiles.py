"""Scripts to read the files with different system"""

# normal file reading 
# open() -  opens file with the defined permission 
# read() - reads the file with specifed permission as 'r'
# close() - cleans up the workspace by closing the file

files = open("./python-scripting/questions.txt", 'r')
read_file = files.read()

print(read_file)

files.close()

# method 2
# reading files with line by line with the .strip()
# .strip() function removed the new line charcter

file2 = open("./python-scripting/questions.txt")
for line in file2:
    print(line.strip())

file2.close()

# method 3 reading files with the readline() one by one
file3 = open("./python-scripting/questions.txt")
line = file3.readline()

while line:
    print(line.strip()) # print the line without the new line charachter by .strip() 
    line = file3.readline() # read the next line 

file3.close()

# method 4 reading the file in binary mode
file4 = open("./python-scripting/questions.txt", 'rb')
content = file4.read()

print(content)

file4.close()

# reading the json and csv files in python 
import csv

# open the csv file 
with open("./python-scripting/demo.csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)

    # read the each line and print 
    for line in csv_reader:
        print(line, type(line))

# opening the json file and printing the output

import json 

# open the json file 
with open("./python-scripting/demo.json", "r") as demojson:
    data = json.load(demojson)
    print(data)





