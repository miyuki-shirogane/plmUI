import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pageObject.base_page import BasePage
from utils.mock import Mock


class MaterialManagePage(BasePage):
    _base_url = "https://comba-test.teletraan.io/subapp/plm/base/material"


    def create_material_get_name(self):
        mock = Mock()
        material_name = mock.mock_data("name") #名称
        material_code = mock.mock_data("code") #编号
        material_version = mock.mock_data("version") #版本
        material_specification = mock.mock_data("specification") #规格型号
        material_unit = mock.mock_data("unit") #计量单位
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR,'.MuiBox-root.jss9>button').click()
        self.driver.find_element(By.XPATH,'//input[@name="name"]').send_keys(material_name)
        self.driver.find_element(By.XPATH,'//input[@name="code"]').send_keys(material_code)
        self.driver.find_element(By.XPATH, '//input[@name="versions"]').send_keys(material_version)
        self.driver.find_element(By.XPATH,'//input[@name="unit"]').send_keys(material_unit)
        self.driver.find_element(By.XPATH, '//div[label="*物料名称"]/ancestor::div//input[@name="property"]').click() #物料属性
        self.driver.find_element(By.XPATH, '//div[@class="MuiAutocomplete-popper"]//li[4]').click()

        self.driver.find_element(By.XPATH,'//button[span="确定"]').click()
        time.sleep(3)
        return material_name

    def get_material_new(self):
        try:
            get_material_name_ele = self.driver.find_element(By.XPATH, '//tr/td[1]')
            get_material_name = get_material_name_ele.text
            return get_material_name
        except:
            raise NoSuchElementException('Seems create material failed')

