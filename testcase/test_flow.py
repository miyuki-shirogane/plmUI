from pageObject.flow_page import FlowPage


class TestFlow:
    def setup_class(self):
        self.flow = FlowPage()

    def test_watch_bom_directly(self):
        res = self.flow.create_flow()
        print(res)

    def teardown_class(self):
        self.flow.driver.quit()
