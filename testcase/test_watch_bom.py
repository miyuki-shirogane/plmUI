from pageObject.bom_page import BOMPage


class TestWatchBom:
    def setup_class(self):
        self.bom = BOMPage()




    def test_watch_bom_directly(self):
        res = self.bom.get_new()
        print(res)



    def teardown_class(self):
        self.bom.driver.quit()
