from pageObject.material_category_page import MaterialCategoryPage


class TestCreateMaterialCategory:
    def setup_class(self):
        self.mat_cg = MaterialCategoryPage()

    def test(self):
        pass

    def teardown(self):
        self.mat_cg.driver.quit()