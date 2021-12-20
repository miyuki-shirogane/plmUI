from random import randint
from hamcrest import *
from pageObject.material_category_page import MaterialCategoryPage


class TestCreateMaterialCategory:
    def setup_class(self):
        self.mat_cg = MaterialCategoryPage()

    def test_create_material_category(self):
        create_name = self.mat_cg.create_material_category_get_name(randint(1, 4))
        get_name = self.mat_cg.get_first_material_category_name()
        assert_that(get_name, equal_to(create_name))

    def test_update_material_category(self):
        update_name = self.mat_cg.update_material_category_get_name()
        get_name = self.mat_cg.get_first_material_category_name()
        assert_that(get_name, equal_to(update_name))

    def teardown(self):
        self.mat_cg.driver.quit()
