# How to write import statements
# build-in library
import collections
import os
import sys

# third party
import termcolor

# our own library
import lesson_package

print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(sys.path)