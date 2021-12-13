from pageObject.material_category_page import MaterialCategoryPage
from pageObject.material_manage_page import MaterialManagePage


class TestCreateMaterial:
    def setup_class(self):
        self.mat_mng = MaterialManagePage()
        self.mat_cg = MaterialCategoryPage()


    '''
    之后不再这样弄。默认基础数据都是有的。
    这里只是示范下多个页面联动 该怎么写；
    '''
    def test_create_material(self):
        material_create = self.mat_cg.create_material_category().goto_material_manage().create_material_get_name()
        material_get = self.mat_mng.get_material_new()
        assert material_create == material_get




    def teardown_class(self):
        self.mat_mng.driver.quit()
