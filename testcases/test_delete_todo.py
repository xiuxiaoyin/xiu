#DELETE方法

import requests 
import pytest
import allure
from common.config import BASE_URL
from common.http_client import delete

#删除待办
@allure.epic("待办事项 API")
@allure.feature("删除待办")
@allure.story("删除成功")
def test_delete_todo_success(temp_todo):
    r = delete(f"/todos/{temp_todo['id']}")
    assert r.status_code == 204

    # 关键：再查一次，确认真的没了
    r2 = requests.get(f"{BASE_URL}/todos/{temp_todo['id']}")
    assert r2.status_code == 404

#删除待办，id不存在->404
@allure.epic("待办事项 API")
@allure.feature("删除待办")
@allure.story("id不存在")
def test_delete_todo_fail_99():
    r = delete("/todos/99")
    assert r.status_code == 404
    assert r.json()["message"] == "todo not found"

# 删除待办，id不是数字->400
@allure.epic("待办事项 API")
@allure.feature("删除待办")
@allure.story("id不是数字")
def test_delete_todo_fail_abc():
    r = delete("/todos/abc")
    assert r.status_code == 400
    assert r.json()["message"] == "id 必须是数字"