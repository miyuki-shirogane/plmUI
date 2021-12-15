import time

from selenium.webdriver.common.by import By
from pageObject.base_page import BasePage
from utils.mock import Mock


class ProjectPage(BasePage):
    _base_url = 'https://comba-test.teletraan.io/subapp/plm/project'

    def create_project_get_name(self):
        self.driver.implicitly_wait(5)
        mock = Mock()
        project_name = mock.mock_data("project_name")
        project_code = mock.mock_data("project_code")
        self.driver.find_element(By.XPATH, '//button[span="项目立项"]').click()
        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(project_name)
        self.driver.find_element(By.XPATH, '//input[@name="code"]').send_keys(project_code)
        self.driver.find_element(By.XPATH, '//div[label="*项目名称"]/ancestor::div//input[@name="projectGroup"]').click()
        self.driver.find_element(By.XPATH, '//div[@class="MuiAutocomplete-popper"]//li[1]').click()
        self.driver.find_element(By.XPATH, '//div[label="*项目名称"]/ancestor::div//input[@name="category"]').click()
        self.driver.find_element(By.XPATH, '//div[@class="MuiAutocomplete-popper"]//li[1]').click()
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        time.sleep(1)
        return project_name

    def add_product_to_project(self, pro_name: str):
        mock = Mock()
        material_name = mock.mock_data("name")  # 名称
        material_code = mock.mock_data("code")  # 编号
        material_version = mock.mock_data("version")  # 版本
        material_unit = mock.mock_data("unit")  # 计量单位
        detail_enter_xpath = f'//td[text()="{pro_name}"]/ancestor::tr//button[@title="查看详情"]'
        self.driver.find_element(By.XPATH, detail_enter_xpath).click()
        self.driver.find_element(By.XPATH, '//button[span="研发产品"]').click()
        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(material_name)
        self.driver.find_element(By.XPATH, '//input[@name="code"]').send_keys(material_code)
        self.driver.find_element(By.XPATH, '//input[@name="versions"]').send_keys(material_version)
        self.driver.find_element(By.XPATH, '//input[@name="unit"]').send_keys(material_unit)
        self.driver.find_element(By.XPATH, '//button[span="保存"]').click()
        time.sleep(1)


