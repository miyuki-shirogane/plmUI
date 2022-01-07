from hamcrest import *
from pageObject.project_page import ProjectPage


class TestProject:
    def setup(self):
        self.pro_mng = ProjectPage()

    def test_create_project(self):
        expect = self.pro_mng.create_project_get_name(project_category="新品定制")
        real = self.pro_mng.get_list_n_column_value(n=1)
        assert_that(real, equal_to(expect))

    def test_create_project_group_option(self):
        expect = self.pro_mng.goto_group_setting().get_all_groups()
        real = self.pro_mng.goto_project().create_project_form_get_group_options()
        assert_that(real, equal_to(expect))

    def test_start_without_product(self):
        name = self.pro_mng.create_project_get_name(project_category="新品定制")
        real = self.pro_mng.status_pending_to_inprocess(pro_name=name).get_alert()
        expect = "启动项目需要先设置研发产品"
        assert_that(real, equal_to(expect))

    def test_start_with_product(self):
        name = self.pro_mng.create_project_get_name(project_category="新品定制")
        self.pro_mng.add_product_to_project(pro_name=name, pro_category="新品定制")
        real = self.pro_mng.goto_project().status_pending_to_inprocess(pro_name=name).get_alert()
        expect = "项目启动成功"
        assert_that(real, equal_to(expect))

    # category = "upgrade",还没测，要等BOM那个函数写完，到时测试下
    def test_check_product_options(self):
        name = self.pro_mng.create_project_get_name(project_category="工艺优化")
        real = self.pro_mng.get_product_options(pro_name=name)
        expect = self.pro_mng.goto_bom().get_product_of_released_bom()
        assert_that(real, equal_to(expect))

    def test_add_task(self):
        project = self.pro_mng.create_project_get_name(project_category="新品定制")
        ls = self.pro_mng.goto_flow().create_flow()
        flow = ls[0]
        real = self.pro_mng.goto_project().add_task_to_project(pro_name=project, flow_name=flow).\
            goto_project().get_first_task_of_project(pro_name=project)
        expect = ls[1]
        assert_that(real, equal_to(expect))

    def test_check_task_act_buttons_under_pending(self):
        name = self.pro_mng.create_project_get_name(project_category="新品定制")
        ls = self.pro_mng.goto_flow().create_flow()
        flow = ls[0]
        real = self.pro_mng.goto_project().add_task_to_project(pro_name=name,flow_name=flow).\
            goto_project().get_len_acts_of_tasks(pro_name=name)
        expect = 1
        assert_that(real, equal_to(expect))

    def test_check_task_act_buttons_under_inprocess(self):
        name = self.pro_mng.create_project_get_name(project_category="新品定制")
        ls = self.pro_mng.goto_flow().create_flow()
        flow = ls[0]
        real = self.pro_mng.goto_project().add_product_to_project(pro_name=name, pro_category="新品定制").\
            goto_project().add_task_to_project(pro_name=name, flow_name=flow).\
            goto_project().status_pending_to_inprocess(pro_name=name).\
            goto_project().get_len_acts_of_tasks(pro_name=name)
        expect = 2
        assert_that(real, equal_to(expect))

    def test_create_bom(self):
        name = self.pro_mng.create_project_get_name(project_category="新品定制")
        ls = self.pro_mng.goto_flow().create_flow()
        flow = ls[0]
        real = self.pro_mng.goto_project().add_product_to_project(pro_name=name, pro_category="新品定制").\
            goto_project().add_task_to_project(pro_name=name, flow_name=flow).\
            goto_project().status_pending_to_inprocess(pro_name=name).\
            goto_project().create_bom(pro_name=name, create_time=3)
        expect = self.pro_mng.goto_project().get_first_bom_of_project(pro_name=name)
        assert_that(real, equal_to(expect))

    # 以下两条删改的用例将沿用上面的数据，故不可以单独执行
    def test_update_bom(self):
        name = self.pro_mng.get_list_n_column_value(n=1)
        real = self.pro_mng.goto_project().update_bom(pro_name=name)
        expect = self.pro_mng.goto_project().get_first_bom_of_project(pro_name=name)
        assert_that(real, equal_to(expect))

    def test_delete_bom(self):
        name = self.pro_mng.get_list_n_column_value(n=1)
        before_delete = self.pro_mng.goto_project().get_first_bom_of_project(pro_name=name)
        after_delete = self.pro_mng.goto_project().delete_bom(pro_name=name).get_first_bom_of_project(pro_name=name)
        assert_that(before_delete, not_(equal_to(after_delete)))

    def test_fill_bom_and_form_interaction(self):
        pass

    def test_task_attachment(self):
        pass

    def test_end_project_with_released_bom(self):
        pass

    def test_end_project_without_released_bom(self):
        pass

    def teardown(self):
        self.pro_mng.driver.quit()