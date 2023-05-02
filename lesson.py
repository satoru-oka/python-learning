# __name__ and __main
import lesson_package.talk.animal
import main

def main():
    lesson_package.talk.animal.sing()

if __name__ == '__main__':
    main()