import string

with open('design/email_template.txt') as f:
    tempfile = string.Template(f.read())

contents = tempfile.substitute(name='Satoru', contents='How ar you?')
print(contents)