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
        before_delete = self.group.get_new_member()
        self.group.delete_member()
        after_delete = self.group.get_new_member()
        assert_that(before_delete, not_(equal_to(after_delete)))

    def test_delete_group(self):
        before_delete = self.group.get_new_group()
        self.group.delete_group()
        after_delete = self.group.get_new_group()
        assert_that(before_delete, not_(equal_to(after_delete)))

    def teardown_class(self):
        self.group.driver.quit()
