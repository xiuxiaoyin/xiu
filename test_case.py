import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"

# # 用例：创建待办成功->201
# def test_create_todo_success():
#     r = requests.post(f"{BASE_URL}/todos", json={"title": "买菜"})
#     assert r.status_code == 201

# # 用例：创建待办,title缺失->400
# def test_create_todo_fail():
#     r = requests.post(f"{BASE_URL}/todos", json={})
#     assert r.status_code == 500
#     assert r.json()["message"] == "title字段不在字典里"      # 或者
#     assert "title" in r.json()["message"]                   # 查消息内容

# # 用例：获取列表成功->200
# def test_get_todos_success():
#     r = requests.get(f"{BASE_URL}/todos")
#     assert r.status_code == 200
#     assert isinstance(r.json(), list)      # 返回的必须是列表

# # 用例：获取单条，id不存在->404
# def test_get_todo_fail_99():
#     r = requests.get(f"{BASE_URL}/todos/99")
#     assert r.status_code == 404
#     assert r.json()["message"] == "todo not found"

# # 用例：获取单条，id不是数字->400
# def test_get_todo_fail_abc():
#     r = requests.get(f"{BASE_URL}/todos/abc")
#     assert r.status_code == 400
#     assert r.json()["message"] == "id 必须是数字"



@pytest.fixture
def temp_todo():
    # ↓ 前置：准备一条数据
    r = requests.post(f"{BASE_URL}/todos", json={"title": "临时数据"})
    todo = r.json()

    yield todo                                    # ← 把数据交给用例

    # ↓ 后置：用例跑完，清理掉
    requests.delete(f"{BASE_URL}/todos/{todo['id']}")


#获取单条待办
def test_get_single_todo(temp_todo):              # ← 名字对上就自动注入
    r = requests.get(f"{BASE_URL}/todos/{temp_todo['id']}")
    assert r.status_code == 200
    assert r.json()["id"] == temp_todo["id"]
    assert r.json()["title"] == "临时数据"


#更新待办列表
def test_update_todo(temp_todo):
    r = requests.put(f"{BASE_URL}/todos/{temp_todo['id']}", json={"title":"学习Java", "completed":True})
    assert r.status_code == 200
    assert r.json()["id"] == temp_todo["id"]
    assert r.json()["title"] == "学习Java"          # 标题改了
    assert r.json()["completed"] is True            # 布尔值也改了
