import time

from selenium.webdriver.common.by import By
from pageObject.base_page import BasePage
from utils.env import Environment
from utils.mock import Mock


class ProjectPage(BasePage):
    env = Environment()
    _base_url = env.url(module="project")

    def create_project_get_name(self, project_category: str):
        mock = Mock()
        plan_date = mock.current_date()
        create_project_attachment = mock.attachment_path(attachment_name="create_project.jpeg")
        project_name = mock.mock_data("project_name")
        project_code = mock.mock_data("project_code")
        self.driver.find_element(By.XPATH, '//button[span="项目立项"]').click()
        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(project_name)
        self.driver.find_element(By.XPATH, '//input[@name="code"]').send_keys(project_code)
        self.driver.find_element(By.XPATH, '//div[label="*项目名称"]/ancestor::div//input[@name="projectGroup"]').click()
        self.driver.find_element(By.XPATH, '//div[@class="MuiAutocomplete-popper"]//li[1]').click()
        self.driver.find_element(By.XPATH, '//div[label="*项目名称"]/ancestor::div//input[@name="category"]').click()
        self.driver.find_element(By.XPATH, f'//span[contains(text(),"{project_category}")]').click()
        self.driver.find_element(By.XPATH,
                                 '//label[contains(text(),"计划开始日期")]/parent::div//input').send_keys(plan_date)
        ele = self.driver.find_element(By.XPATH, '//label[contains(text(),"立项文档")]/parent::div//input')
        ele.send_keys(create_project_attachment)
        time.sleep(2)
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


