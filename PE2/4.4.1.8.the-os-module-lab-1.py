#!/usr/bin/env python3

# 4.4.1.8 The os module: LAB
# It goes without saying that operating systems allow you to search for files and directories.
# While studying this part of the course, you learned about the functions of the os module, 
# which have everything you need to write a program that will search for directories in a given location.

# To make your task easier, we have prepared a test directory structure for you:
# see image: 4.4.1.8.png

# Your program should meet the following requirements:
#   Write a function or method called find that takes two arguments called path and dir.
#     The path argument should accept a relative or absolute path to a directory where the search should start, 
#     while the dir argument should be the name of a directory that you want to find in the given path.
#     Your program should display the absolute paths if it finds a directory with the given name.
#   The directory search should be done recursively.
#     This means that the search should also include all subdirectories in the given path.
# 
# Example input:
# path="./tree", dir="python"
# 
# Example output:
# .../tree/python
# .../tree/cpp/other_courses/python
# .../tree/c/other_courses/python

# to match directory structure:
#   mkdir -p tree/c/other_courses/cpp
#   mkdir -p tree/c/other_courses/python
#   mkdir -p tree/cpp/other_courses/c
#   mkdir -p tree/cpp/other_courses/python
#   mkdir -p tree/python/other_courses/c
#   mkdir -p tree/python/other_courses/cpp

import os

def find(path, dir):
    os.chdir(path)
    current_dir = os.getcwd()
    for item in os.listdir("."):
        if item == dir:
            print(os.getcwd() + "/" + dir)
        find(current_dir + "/" + item, dir)

find("./tree", "python")
