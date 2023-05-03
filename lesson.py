# request
import requests

payload = {'key1': 'value1', 'key2': 'value2'}

# response = requests.get('http://httpbin.org./get', params=payload)
# response = requests.post('http://httpbin.org./post', params=payload)
# response = requests.put('http://httpbin.org./put', params=payload)
response = requests.delete('http://httpbin.org./delete', params=payload, timeout=1)

print(response.status_code)
print(response.text)
print(response.json())

