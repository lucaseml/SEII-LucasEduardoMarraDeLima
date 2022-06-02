#Lucas Eduardo Marra de Lima

import my_module

courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Math')
print(index)

print("\n")
from my_module import find_index, test
import sys

index = find_index(courses, 'Math')
print(index, test)

print("\n")
print(sys.path)

print("\n")
import os
print(os.getcwd())

import webbrowser
import hashlib
webbrowser.open("https://www.youtube.com/watch?v=CqvZ3vGoGs0&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=9&ab_channel=CoreySchafer")