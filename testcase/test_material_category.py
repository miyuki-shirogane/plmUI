from pageObject.material_category_page import MaterialCategoryPage


class TestCreateMaterialCategory:
    def setup_class(self):
        self.mat_cg = MaterialCategoryPage()

    #测试下contributions会不会绿
    def test(self):
        pass

    def teardown(self):
        self.mat_cg.driver.quit()