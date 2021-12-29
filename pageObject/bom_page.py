from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pageObject.base_page import BasePage
from utils.env import Environment


class BOMPage(BasePage):
    env = Environment()
    _base_url = env.url(module="bom")

    def get_new(self):
        self.driver.implicitly_wait(5)
        try:
            ele = self.driver.find_element(By.CSS_SELECTOR, '.MuiTableBody-root td:nth-child(3)')
            bom_version = ele.text
            return bom_version
        except:
            raise NoSuchElementException("This page has no BOM for now")
