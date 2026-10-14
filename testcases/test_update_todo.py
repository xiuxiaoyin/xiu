#PUT方法

import requests
import pytest
import allure
from common.config import BASE_URL
from common.http_client import put

#更新待办列表
@allure.epic("待办事项 API")        # 最顶层：整个项目
@allure.feature("更新单条待办")          # 一个功能模块
@allure.story("更新成功")            # 功能下的一个场景组
def test_update_todo(temp_todo):
    r = put(f"/todos/{temp_todo['id']}", json={"title":"学习Java", "completed":True})
    assert r.status_code == 200
    assert r.json()["id"] == temp_todo["id"]
    assert r.json()["title"] == "学习Java"          # 标题改了
    assert r.json()["completed"] is True            # 布尔值也改了