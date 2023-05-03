#  tempfile
import tempfile

with tempfile.TemporaryFile(mode="w+") as tmp:
    tmp.write('hello')
    tmp.seek(0)
    print(tmp.read())

with tempfile.NamedTemporaryFile(delete=False) as tmp:
    print(tmp.name)
    with open(tmp.name, 'w+') as file:
        file.write('test\n')
        file.seek(0)
        print(file.read())

with tempfile.TemporaryDirectory() as tmpdir:
    print(tmpdir)

temp_dir = tempfile.mkdtemp()
print(temp_dir)