"""
测试点：
物料管理增删改查，以及表单里面的类别筛选
"""
import pytest
from pageObject.material_manage_page import MaterialManagePage


class TestCreateMaterial:
    def setup(self):
        self.mat_mng = MaterialManagePage()

    @pytest.mark.parametrize("n", [1, 2, 3, 4], ids=["产品", "原辅料", "中间体", "菌种"])
    def test_get_option(self, n: int):
        actual_options = self.mat_mng.goto_material_category().get_materials_category_search(pick_num_category_filter=n)
        category_options = self.mat_mng.goto_material_manage().create_material_form_get_category(
            pick_num_material_form=n)
        print(category_options, category_options)
        assert category_options == actual_options

    def test_create_material(self):
        create_name = self.mat_mng.create_material_get_name()
        get_name = self.mat_mng.get_material_new()
        print(create_name, get_name)
        assert create_name == get_name

    def test_update_material(self):
        update_name = self.mat_mng.update_material_get_name()
        get_name = self.mat_mng.get_material_new()
        print(update_name, get_name)
        assert update_name == get_name

    def test_delete_material(self):
        # delete_name = self.mat_mng.get_material_new()
        after_delete_name = self.mat_mng.delete_material()
        print(after_delete_name)
        # assert delete_name != after_delete_name

    def teardown(self):
        self.mat_mng.driver.quit()
