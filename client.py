import requests

#POST创建待办
c = requests.post("http://127.0.0.1:5000/todos",json={"title":"学习Python"})
print(c.status_code)
print(c.text)

#GET全部待办列表
r = requests.get("http://127.0.0.1:5000/todos")
print(r.status_code)
print(r.text)

#GET匹配的id的待办
r = requests.get("http://127.0.0.1:5000/todos/1")
print(r.status_code)
print(r.text)

#PUT更新匹配的id的待办
p = requests.put("http://127.0.0.1:5000/todos/1",json={"title":"学习Java", "completed":True})
print(p.status_code)
print(p.text)

#DELETE删除匹配的id的待办
d = requests.delete("http://127.0.0.1:5000/todos/1")
print(d.status_code)
print(d.text)

#GET匹配的id的待办
r = requests.get("http://127.0.0.1:5000/todos/1")
print(r.status_code)
print(r.text)