from hamcrest import *

from pageObject.group_setting_page import GroupSettingPage


class TestGroupSetting:
    def setup(self):
        self.group = GroupSettingPage()

    def test_add_group(self):
        expect = self.group.add_group()
        real = self.group.get_new_group()
        assert_that(real, equal_to(expect))

    def test_add_member(self):
        self.group.add_group()
        expect = self.group.add_member()
        real = self.group.get_new_member()
        assert_that(real, equal_to(expect))

    def test_delete_member(self):
        self.group.delete_member()
        real = self.group.get_alert()
        expect = "移除成功！"
        assert_that(real, equal_to(expect))

    """
    删除小组分为以下3个case：
    a.创建、删除：删除成功
    b.创建、添加组员、删除：当前小组存在组员数据，无法删除
    c.创建、项目引用、删除：当前小组已被使用，无法删除
    """
    def test_delete_group_a(self):
        self.group.add_group()
        self.group.delete_group()
        real = self.group.get_alert()
        expect = "删除成功"
        assert_that(real, equal_to(expect))

    def test_delete_group_b(self):
        self.group.add_group()
        self.group.add_member()
        self.group.delete_group()
        real = self.group.get_alert()
        expect = "当前小组存在组员数据，无法删除"
        assert_that(real, equal_to(expect))

    def test_delete_group_c(self):
        self.group.add_group()
        self.group.goto_project().create_project_get_name(project_category="新品定制")
        self.group.goto_group_setting().delete_group()
        real = self.group.get_alert()
        expect = "当前小组已被使用，无法删除"
        assert_that(real, equal_to(expect))

    def teardown(self):
        self.group.driver.quit()
