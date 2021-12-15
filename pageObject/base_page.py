import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.mock import Mock


class BasePage:

    def __init__(self,base_driver = None):
        _base_url = None

        if base_driver:
            self.driver = base_driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            if self._base_url != None:
                self.driver.get(self._base_url)
                self.driver.find_element(By.XPATH,"//input[@name='account']").send_keys("Caitlyn")
                self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Caitlyn")
                self.driver.find_element(By.CSS_SELECTOR,".MuiButton-label").click()
            else:
                pass

    def goto_BOM(self):
        self.driver.find_element(By.XPATH,"//ul/div[2]").click()
        from pageObject.bom_page import BOMPage
        return BOMPage(self.driver)

    def goto_material_manage(self):
        self.driver.find_element(By.XPATH,"//ul/div[5]//div[@role='button'][1]").click()
        from pageObject.material_manage_page import MaterialManagePage
        time.sleep(1)
        return MaterialManagePage(self.driver)

    def goto_material_category(self):
        self.driver.find_element(By.XPATH,"//ul/div[5]//div[@role='button'][2]").click()
        from pageObject.material_category_page import MaterialCategoryPage
        time.sleep(1)
        return MaterialCategoryPage(self.driver)

    def goto_project(self):
        self.driver.find_element(By.XPATH, "//ul/div[1]").click()
        from pageObject.project_page import ProjectPage
        time.sleep(1)
        return ProjectPage(self.driver)
