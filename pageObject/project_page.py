from pageObject.base_page import BasePage
from pageObject.bom_page import BOMPage


class ProjectPage(BasePage):
    _base_url = 'https://comba-test.teletraan.io/subapp/plm/project'

    def start(self):
        pass
        return BOMPage(self.driver)
