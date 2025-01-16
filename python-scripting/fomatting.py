import black
from pathlib import Path

script = input("Enter the script name with .py extension you want to format: ")

# Ensure the script exists before formatting
if Path(script).is_file():
    with open(script, "r") as file:
        source_code = file.read()
    
    # Format the code
    formatted_code = black.format_file_contents(source_code, fast=False, mode=black.FileMode())
    
    # Save the formatted code back to the file
    with open(script, "w") as file:
        file.write(formatted_code)
    
    print(f"Formatted {script} using Black.")
else:
    print(f"The file {script} does not exist.")
