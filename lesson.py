# seek
s = """\
ABC
DEF
GHI
JKN
"""
with open('test.txt', 'r') as is_file:
    # print(is_file.tell())
    print(is_file.read(1))
    is_file.seek(1)
    print(is_file.read(1))
    is_file.seek(2)
    print(is_file.read(1))
    is_file.seek(4)
    print(is_file.read(1))
    is_file.seek(8)
    print(is_file.read(1))
