import black
import os
import sys
script = str(input("Enter the script name with .py extension you want to format: "))

os.system(black(script))