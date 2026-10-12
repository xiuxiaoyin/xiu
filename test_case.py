import requests
import pytest
import yaml
import allure

BASE_URL = "http://127.0.0.1:5000"

def load_cases(path):
    #读取一个 YAML 文件，并把它解析成 Python 对象（通常是字典或列表）返回
    with open(path,encoding="utf-8") as f:
        return yaml.safe_load(f)
CASES = load_cases("test_data/create_todo_validation.yml")

def clear_all_todos():
    """清空所有待办"""
    r = requests.get(f"{BASE_URL}/todos")
    for todo in r.json():
        requests.delete(f"{BASE_URL}/todos/{todo['id']}")

@pytest.fixture(autouse=True)       #autouse=True 的意思是：不用在用例参数里写名字，每条用例自动生效
def clean_env():
    clear_all_todos()        # ← 前置：保证从干净状态开始
    yield
    clear_all_todos()        # ← 后置：跑完不留垃圾

@pytest.fixture
def temp_todo():
    # ↓ 前置：准备一条数据
    r = requests.post(f"{BASE_URL}/todos", json={"title": "临时数据"})
    todo = r.json()
    yield todo          # ← 把数据交给用例
    # ↓ 后置：用例跑完，清理掉
    requests.delete(f"{BASE_URL}/todos/{todo['id']}")

#post参数化
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("创建待办")          # 一个功能模块
@allure.story("参数校验")            # 功能下的一个场景组
@pytest.mark.parametrize("case", CASES, ids=[c["case_name"] for c in CASES])
def test_create_todo_fail(case):
    r = requests.post(f"{BASE_URL}/todos", json=case["body"])
    assert r.status_code == 400
    assert r.json()["message"] == case["expected_message"]

# 用例：创建待办成功->201
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("创建待办")          # 一个功能模块
@allure.story("创建成功")            # 功能下的一个场景组
def test_create_todo_success():
    r = requests.post(f"{BASE_URL}/todos", json={"title": "买菜"})
    assert r.status_code == 201
    assert isinstance(r.json()["id"], int)      # 是个整数就行，不关心具体是几
    assert r.json()["title"] == "买菜"
    assert r.json()["completed"] is False   

# 用例：获取列表成功->200
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("获取待办列表")          # 一个功能模块
@allure.story("成功场景")            # 功能下的一个场景组
def test_get_todos_success(temp_todo):
    r = requests.get(f"{BASE_URL}/todos")
    assert r.status_code == 200
    assert len(r.json()) == 1                  # 干净环境里只有 1 条
    assert r.json()[0]["id"] == temp_todo["id"]      # 就是刚创建那条

# 用例：获取单条，id不存在->404
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("获取单条待办")          # 一个功能模块
@allure.story("id不存在")            # 功能下的一个场景组
def test_get_todo_fail_99():
    r = requests.get(f"{BASE_URL}/todos/99")
    assert r.status_code == 404
    assert r.json()["message"] == "todo not found"

# 用例：获取单条，id不是数字->400
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("获取单条待办")          # 一个功能模块
@allure.story("id不是数字")            # 功能下的一个场景组
def test_get_todo_fail_abc():
    r = requests.get(f"{BASE_URL}/todos/abc")
    assert r.status_code == 400
    assert r.json()["message"] == "id 必须是数字"

#获取单条待办
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("获取单条待办")          # 一个功能模块
@allure.story("获取成功")            # 功能下的一个场景组
def test_get_single_todo(temp_todo):              # ← 名字对上就自动注入
    r = requests.get(f"{BASE_URL}/todos/{temp_todo['id']}")
    assert r.status_code == 200
    assert r.json()["id"] == temp_todo["id"]
    assert r.json()["title"] == "临时数据"

#更新待办列表
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("更新单条待办")          # 一个功能模块
@allure.story("更新成功")            # 功能下的一个场景组
def test_update_todo(temp_todo):
    r = requests.put(f"{BASE_URL}/todos/{temp_todo['id']}", json={"title":"学习Java", "completed":True})
    assert r.status_code == 200
    assert r.json()["id"] == temp_todo["id"]
    assert r.json()["title"] == "学习Java"          # 标题改了
    assert r.json()["completed"] is True            # 布尔值也改了
