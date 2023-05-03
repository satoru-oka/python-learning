# file read and write
s = """\
ABC
DEF
GHI
JKN
"""
with open('test.txt', 'w+') as is_file:
    is_file.write(s)
    is_file.seek(0) # back to start
    print(is_file.read())

with open('test.txt', 'r+') as is_file:
    print(is_file.read())
    is_file.seek(0)
    is_file.write(s)