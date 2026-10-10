import requests

r = requests.get("https://httpbin.org/get?name=xiu",json = {"name":"xiu","job":"测试开发"})
print(r.status_code)
print(r.text)