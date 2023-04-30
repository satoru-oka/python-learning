# Variable declaration
num = 1
name = 'Mike'
is_ok = True

# type() - Confirmation of type
print(num, type(num)) # int
print(name, type(name)) # str
print(is_ok, type(is_ok)) # bool

# Ok to overwrite values
num_1 = 1
name_str = '1'

num_1 = name_str
print(num_1, type(num_1)) # print string

# type conversion
new_num = int(num_1)
print(num_1, type(new_num))
