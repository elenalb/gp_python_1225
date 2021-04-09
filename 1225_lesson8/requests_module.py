# requests
import requests

# создание запроса
url = "https://github.com/requests"
resp = requests.get(url)
print(resp)
print(resp.status_code)
print(resp.headers)
print(resp.text)
print(type(resp))

resp = requests.put(f"{url}/put")
print(resp)

resp = requests.delete(f"{url}/delete")
print(resp)

# data = {'key1': 'value1'}
# resp = requests.get(f"{url}/get", param=data)
