"""
Write a script to count the number of lines in a file.

"""

def count_lies(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
            return len(content)
    except FileNotFoundError:
        print(f"The file specified '{file_path}' does not exists")
        return None
    except Exception as e:
        print(f"Unexpected error occured '{e}'.")
        return None

def main():
    context = str(input("Enter the file name with path and press enter: "))
    print(count_lies(context))

if __name__ == "__main__":
    main()
    
    
