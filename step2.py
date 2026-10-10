import requests

r = requests.post("https://httpbin.org/post",data="hello")
print(r.status_code)
print(r.text)