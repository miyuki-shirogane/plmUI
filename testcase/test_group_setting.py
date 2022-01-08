from hamcrest import *

from pageObject.group_setting_page import GroupSettingPage


class TestGroupSetting:
    def setup_class(self):
        self.group = GroupSettingPage()

    def test_add_group(self):
        expect = self.group.add_group()
        real = self.group.get_new_group()
        assert_that(real, equal_to(expect))

    def test_add_member(self):
        expect = self.group.add_member()
        real = self.group.get_new_member()
        assert_that(real, equal_to(expect))

    def test_delete_member(self):
        self.group.delete_member()
        real = self.group.get_alert()
        expect = "移除成功！"
        assert_that(real, equal_to(expect))

    def test_delete_group(self):
        self.group.add_group()
        self.group.delete_group()
        real = self.group.get_alert()
        expect = "删除成功"
        assert_that(real, equal_to(expect))

    def teardown_class(self):
        self.group.driver.quit()
