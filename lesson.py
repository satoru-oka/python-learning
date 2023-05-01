# import lesson_package.utils
from lesson_package.tools import utils
from lesson_package.talk import human
# from lesson_package import utils as u
# from lesson_package import utils say_twice

# r = lesson_package.utils.say_twice('hello')
r = utils.say_twice('hello')
# r = say_twice('hello')

print(r)
print(human.sing())
print(human.cry())