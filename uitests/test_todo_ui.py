import uuid
from playwright.sync_api import Page, expect
from pages.todo_page import TodoPage

def test_add_todo(page: Page):
    todo_page = TodoPage(page)
    title = f"UI-{uuid.uuid4().hex[:8]}"        # 唯一标题，避免和别的数据撞

    todo_page.goto()
    todo_page.add_todo(title)
    todo_page.expect_todo_exists(title)

    # 清理：删掉自己创建的
    todo_page.delete_todo(title)
    todo_page.expect_todo_not_exists(title)


def test_complete_todo(page: Page, temp_todo):
    todo_page = TodoPage(page)
    todo_page.goto()

    todo_page.complete_todo(temp_todo["title"])
    todo_page.expect_completed(temp_todo["title"])

    page.reload()                                    # 刷新，从服务器重新拉
    todo_page.expect_completed(temp_todo["title"])

def test_delete_todo(page: Page, temp_todo):
    # TODO: 打开页面
    # TODO: 找到 temp_todo 对应的那条，点它的删除按钮
    # TODO: 断言那条从页面上消失了
    todo_page = TodoPage(page)
    todo_page.goto()
    todo_page.delete_todo(temp_todo["title"])
    todo_page.expect_todo_not_exists(temp_todo["title"])