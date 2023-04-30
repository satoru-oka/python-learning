# string method
s = 'My name is Satoru. Hi Satoru'
print(s)

# Is the specified string at the beginning?
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('name')
print(is_start)
print("##########")
# start
print(s.find('Satoru'))
# end
print(s.rfind('Satoru'))
print(s.count('Satoru'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Satoru', 'Oka'))