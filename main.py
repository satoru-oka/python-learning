# key word arg
def menu(entree='beef', drink='wine'):
    print(entree, drink)

menu(entree='beef', drink='coffee')

def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffee')

is_dict = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'desert': 'ice'
}
menu(**is_dict)

def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana', 'apple', 'remon', drink='tropical', desert='ice')