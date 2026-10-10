import requests

r = requests.get("https://httpbin.org/get")
print(r.status_code)
print(r.text)
assert r.status_code == 404

