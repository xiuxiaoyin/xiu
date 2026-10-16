#GET方法

import requests
import pytest
import  allure
from common.config import BASE_URL
from common.http_client import get

# 用例：获取列表成功->200
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("获取待办列表")          # 一个功能模块
@allure.story("成功场景")            # 功能下的一个场景组
def test_get_todos_success(temp_todo):
    r = get("/todos")
    assert r.status_code == 200
    ids = [t["id"] for t in r.json()]
    assert temp_todo["id"] in ids

# 用例：获取单条，id不存在->404
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("获取单条待办")          # 一个功能模块
@allure.story("id不存在")            # 功能下的一个场景组
def test_get_todo_fail_99():
    r = get("/todos/99")
    assert r.status_code == 404
    assert r.json()["message"] == "todo not found"

# 用例：获取单条，id不是数字->400
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("获取单条待办")          # 一个功能模块
@allure.story("id不是数字")            # 功能下的一个场景组
def test_get_todo_fail_abc():
    r = get("/todos/abc")
    assert r.status_code == 400
    assert r.json()["message"] == "id 必须是数字"

#获取单条待办
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("获取单条待办")          # 一个功能模块
@allure.story("获取成功")            # 功能下的一个场景组
def test_get_single_todo(temp_todo):              # ← 名字对上就自动注入
    r = get(f"/todos/{temp_todo['id']}")
    assert r.status_code == 200
    assert r.json()["id"] == temp_todo["id"]
    assert r.json()["title"] == "临时数据"