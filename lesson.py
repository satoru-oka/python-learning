# file read
s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt', 'r') as is_file:
    while True:
        chunk = 2
        line = is_file.read(chunk)
        print(line)
        if not line:
            break

with open('test.txt', 'r') as is_file:
    while True:
        line = is_file.readline()
        print(line, end='')
        if not line:
            break