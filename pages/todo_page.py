from playwright.sync_api import Page, expect
from common.config import BASE_URL

class TodoPage:
    def __init__(self, page: Page):
        self.page = page                      # 把浏览器页存起来，后面所有方法都用它

    def goto(self):
        self.page.goto(BASE_URL)

    def _item(self, title):         #定位某条待办
        return self.page.get_by_test_id("todo-item").filter(has_text=title)

    def expect_todo_exists(self, title):            #断言存在
        expect(self.page.get_by_test_id("todo-title").filter(has_text=title)).to_have_count(1)

    def expect_todo_not_exists(self, title):        #断言不存在
        expect(self.page.get_by_test_id("todo-title").filter(has_text=title)).to_have_count(0)

    def add_todo(self, title):      #添加待办
        self.page.get_by_test_id("new-todo-input").fill(title)
        self.page.get_by_test_id("add-button").click()

    def complete_todo(self, title):         #勾选
        self._item(title).get_by_test_id("todo-checkbox").check()

    def expect_completed(self, title):      #勾选断言
        expect(self._item(title).get_by_test_id("todo-checkbox")).to_be_checked()

    def delete_todo(self, title):      #删除待办
        self._item(title).get_by_test_id("delete-button").click()
       