# json
import json

employee = {
    "employee":
        [
            {"id": 111, "name": "satoru"},
            {"id": 222, "name": "ok@"}
        ]
}

print(employee)
print('@@@@@@@@@@')

print('#####')
json_dumps = json.dumps(employee)
print(json.loads(json_dumps))
print('#####')

with open('test.json', 'w') as json_file:
    json.dump(employee, json_file)

print('@@@@@@@@@@')

with open('test.json', 'r') as json_file:
    print(json.load(json_file))

