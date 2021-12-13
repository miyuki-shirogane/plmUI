from random import randint
from selenium.webdriver.common.by import By
from pageObject.base_page import BasePage
from pageObject.material_manage_page import MaterialManagePage
from utils.mock import Mock


class MaterialCategoryPage(BasePage):
    _base_url = "https://comba-test.teletraan.io/subapp/plm/base/category"

    def create_material_category(self,n=randint(1,4)):
        mock = Mock()
        category = mock.mock_data('category_')
        self.driver.find_element(By.XPATH,'//button[span="新增物料类别"]').click()
        self.driver.find_element(By.XPATH, '//div[label="*物料类别"]/ancestor::div//input[@name="property"]').click() #物料属性
        self.driver.find_element(By.XPATH, f'//div[@class="MuiAutocomplete-popper"]//li[{n}]').click()
        self.driver.find_element(By.XPATH,'//input@[name="name"]').send_keys(category)
        self.driver.find_element(By.XPATH,'//button[span="确定"]')
        return MaterialManagePage(self.driver)

    def get_num_of_material_category(self):
        pass

    def edit_material_category(self):
        pass

    def delete_material_category(self):
        pass