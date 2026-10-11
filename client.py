import requests

# #POST创建待办
# c = requests.post("http://127.0.0.1:5000/todos",json={"title":"学习Python"})
# print(c.status_code)
# print(c.text)

#GET全部待办列表
r = requests.get("http://127.0.0.1:5000/todos")
print(r.status_code)
print(r.text)

# #GET匹配的id的待办
# r = requests.get("http://127.0.0.1:5000/todos/1")
# print(r.status_code)
# print(r.text)

# #PUT更新匹配的id的待办
# p = requests.put("http://127.0.0.1:5000/todos/1",json={"title":"学习Java", "completed":True})
# print(p.status_code)
# print(p.text)

# #DELETE删除匹配的id的待办
# d = requests.delete("http://127.0.0.1:5000/todos/1")
# print(d.status_code)
# print(d.text)

# #GET匹配的id的待办
# r = requests.get("http://127.0.0.1:5000/todos/1")
# print(r.status_code)
# print(r.text)

# #POST 空字典
# c = requests.post("http://127.0.0.1:5000/todos",json={})
# print(c.status_code)
# print(c.text)

# #POST title为null
# c = requests.post("http://127.0.0.1:5000/todos",json={"title":None})
# print(c.status_code)
# print(c.text)

# #POST title为数字
# c = requests.post("http://127.0.0.1:5000/todos",json={"title":123})
# print(c.status_code)
# print(c.text)

# #POST title为空串
# c = requests.post("http://127.0.0.1:5000/todos",json={"title":" "})
# print(c.status_code)
# print(c.text)

# #POST title超出长度限制
# c = requests.post("http://127.0.0.1:5000/todos",json={"title":"abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789"})
# print(c.status_code)
# print(c.text)

# #GET /todos/<id>
# r = requests.get("http://127.0.0.1:5000/todos/abc")
# print(r.status_code)
# print(r.text)

# #GET /todos/<id>
# r = requests.get("http://127.0.0.1:5000/todos/0")
# print(r.status_code)
# print(r.text)

# #GET /todos/<id>
# r = requests.get("http://127.0.0.1:5000/todos/999999")
# print(r.status_code)
# print(r.text)

# #GET /todos/<id>
# r = requests.get("http://127.0.0.1:5000/todos/-1")
# print(r.status_code)
# print(r.text)

# #POST null
# c = requests.post(
#     "http://127.0.0.1:5000/todos",
#     data="null",                                    # 原始文本 body
#     headers={"Content-Type": "application/json"}    # 手动告诉服务端这是 JSON
# )
# print(c.status_code, c.text)
