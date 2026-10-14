#POST方法

import requests
import pytest
import allure
from common.config import BASE_URL, CASES
from common.http_client import post

#post参数化
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("创建待办")          # 一个功能模块
@allure.story("参数校验")            # 功能下的一个场景组
@pytest.mark.parametrize("case", CASES, ids=[c["case_name"] for c in CASES])
def test_create_todo_fail(case):
    r = post("/todos", json=case["body"])
    assert r.status_code == 400
    assert r.json()["message"] == case["expected_message"]

# 用例：创建待办成功->201
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("创建待办")          # 一个功能模块
@allure.story("创建成功")            # 功能下的一个场景组
def test_create_todo_success():
    r = post("/todos", json={"title": "买菜"})
    assert r.status_code == 201
    assert isinstance(r.json()["id"], int)      # 是个整数就行，不关心具体是几
    assert r.json()["title"] == "买菜"
    assert r.json()["completed"] is False   