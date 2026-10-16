#共享fixture

import pytest
from common.http_client import get, post, delete

def clear_all_todos():
    """清空所有待办"""
    r = get("/todos")
    for todo in r.json():
        delete(f"/todos/{todo['id']}")

@pytest.fixture
def temp_todo():
    # ↓ 前置：准备一条数据
    r = post("/todos", json={"title": "临时数据"})
    todo = r.json()
    yield todo          # ← 把数据交给用例
    # ↓ 后置：用例跑完，清理掉
    delete(f"/todos/{todo['id']}")
