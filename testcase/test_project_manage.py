from pageObject.project_page import ProjectPage


class TestProject:
    def setup(self):
        self.pro_mng = ProjectPage()

    def test_create_project(self):
        res = self.pro_mng.create_project_get_name()
        print(res)

    # def test_1(self):
    #     self.pro_mng.add_product_to_project("project_name_VTf8nd")

    def teardown(self):
        self.pro_mng.driver.quit()