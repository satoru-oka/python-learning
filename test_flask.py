import requests

response = requests.get('http://127.0.0.1:5000/employee/satoru')
print(response.text)

response = requests.post('http://127.0.0.1:5000/employee', data={'name': 'satoru'})
print(response.text)

response = requests.put('http://127.0.0.1:5000/employee', data={
    'name': 'satoru', 'new_name': 'ok@'})
print(response.text)

response = requests.delete('http://127.0.0.1:5000/employee', data={'name': 'satoru'})
print(response.text)