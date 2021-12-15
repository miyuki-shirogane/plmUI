"""
测试点：
物料管理增删改查，以及表单里面的类别筛选
"""
import logging
import time
import pytest
from hamcrest import *
from pageObject.material_manage_page import MaterialManagePage


class TestMaterial:
    def setup(self):
        self.mat_mng = MaterialManagePage()

    @pytest.mark.parametrize("n", [1, 2, 3, 4], ids=["产品", "原辅料", "中间体", "菌种"])
    def test_get_option(self, n: int):
        actual_options = self.mat_mng.goto_material_category().get_materials_category_search(pick_num_category_filter=n)
        category_options = self.mat_mng.goto_material_manage().create_material_form_get_category(
            pick_num_material_form=n)
        logging.info(f'count_before_delete:{actual_options};count_after_delete:{category_options}')
        assert_that(actual_options, equal_to(category_options))

    def test_create_material(self):
        create_name = self.mat_mng.create_material_get_name()
        get_name = self.mat_mng.get_material_new()
        logging.info(f'count_before_delete:{create_name};count_after_delete:{get_name}')
        assert_that(create_name, equal_to(get_name))

    def test_update_material(self):
        update_name = self.mat_mng.update_material_get_name()
        get_name = self.mat_mng.get_material_new()
        logging.info(f'count_before_delete:{update_name};count_after_delete:{get_name}')
        assert_that(update_name, equal_to(get_name))

    """
    这一块比较复杂，删除的产品设计逻辑如下：
    1.如果物料被项目引用，那么无法删除，且提示："当前物料已被使用，无法删除"。
    2.如果物料没有被引用，那么可以正常删除。
    -------------
    于是，这里的测试用例预备分为2个处理：
    1.创建物料A，删除，预期删除成功，断言方式就看物料list个数吧。。
    2。创建项目(新品研发)并新增产品（物料B），删除，预期删除失败，断言方式同上
    """
    def test_delete_material_b(self):
        # 前置条件
        project_name = self.mat_mng.goto_project().create_project_get_name()
        self.mat_mng.goto_project().add_product_to_project(project_name)
        time.sleep(5)
        count_before_delete = self.mat_mng.goto_material_manage().get_count_of_material()
        # 删除操作
        self.mat_mng.delete_material()
        count_after_delete = self.mat_mng.get_count_of_material()
        logging.info(f'count_before_delete:{count_before_delete};count_after_delete:{count_after_delete}')
        assert_that(count_before_delete, equal_to(count_after_delete))

    def teardown(self):
        self.mat_mng.driver.quit()
