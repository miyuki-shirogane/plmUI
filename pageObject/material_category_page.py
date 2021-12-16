import time
from random import randint
from selenium.webdriver.common.by import By
from pageObject.base_page import BasePage
from utils.mock import Mock


class MaterialCategoryPage(BasePage):
    _base_url = "https://comba-test.teletraan.io/subapp/plm/base/category"

    def create_material_category_get_name(self, pick_num_category_form=randint(1, 4)):
        mock = Mock()
        category_name = mock.mock_data('category_name')
        self.driver.find_element(By.XPATH, '//button[span="新增物料类别"]').click()
        self.driver.find_element(By.XPATH, '//div[label="*物料类别"]/ancestor::div//input[@name="property"]').click()
        self.driver.find_element(By.XPATH, f'//div[@class="MuiAutocomplete-popper"]//li[{pick_num_category_form}]')\
            .click()
        self.driver.find_element(By.XPATH, '//input@[name="name"]').send_keys(category_name)
        self.driver.find_element(By.XPATH, '//button[span="确定"]')
        time.sleep(1)
        return category_name

    # filter="物料属性"，list搜索，获取返回物料类别列表
    def get_materials_category_search(self, pick_num_category_filter: int):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//input[@placeholder="物料属性"]').click()
        self.driver.find_element(By.XPATH, f'//div[@class="MuiAutocomplete-popper"]//li[{pick_num_category_filter}]')\
            .click()
        self.driver.find_element(By.XPATH, '//button[span="查询"]').click()
        time.sleep(3)
        return [i.text for i in self.driver.find_elements(By.XPATH, '//tr/td[2]')]

    def get_material_category_num(self):
        pass

    def edit_material_category(self):
        pass

    def delete_material_category(self):
        pass
