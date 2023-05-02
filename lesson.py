# import lesson_package.utils
# from lesson_package.tools import utils
# from lesson_package.talk import human
# from lesson_package import utils as u
# from lesson_package import utils say_twice
# from lesson_package.talk import *

"""
import error for example.
Older version is a statement of try, newer version is an except statement.
"""
try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

utils.say_twice('word')

# r = lesson_package.utils.say_twice('hello')
# r = utils.say_twice('hello')
# r = say_twice('hello')

# print(r)
# print(human.sing())
# print(human.cry())

# print(animal.sing())
# print(animal.cry())