# urllib.request
import urllib.request
import json

payload = {'key1': 'value1', 'key2': 'value2'}

# url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
# print(url)
# with urllib.request.urlopen(url) as response_file:
#     response = json.loads(response_file.read().decode('utf-8'))
#     print(type(response))
#     print(response)

payload = json.dumps(payload).encode('utf-8')
# req = urllib.request.Request(
#     'http://httpbin.org/post', data=payload, method='POST')
# with urllib.request.urlopen(req) as response:
#     print(json.loads(response.read().decode('utf-8')))

req = urllib.request.Request(
    'http://httpbin.org/put', data=payload, method='PUT')
with urllib.request.urlopen(req) as response:
    print(json.loads(response.read().decode('utf-8')))

req = urllib.request.Request(
    'http://httpbin.org/delete', data=payload, method='DELETE')
with urllib.request.urlopen(req) as response:
    print(json.loads(response.read().decode('utf-8')))

