import requests

r = requests.get("https://httpbin.org/get")
print(r.status_code)
print(r.text)
print(r.headers)
assert r.status_code == 200

