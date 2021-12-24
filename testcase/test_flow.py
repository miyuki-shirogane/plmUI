import logging
from hamcrest import *
from pageObject.flow_page import FlowPage


class TestFlow:
    def setup_class(self):
        self.flow = FlowPage()

    def test_create_flow_and_form_interaction(self):
        expect = self.flow.create_flow()
        real = self.flow.get_flow_and_tasks()
        logging.info(f'\nexpect_flow_and_tasks:{expect};\nreal_flow_and_tasks:{real}')
        assert_that(real, equal_to(expect))

    def test_update_flow_task(self):
        expect = self.flow.update_flow()
        real = self.flow.get_list_n_column_value(2)
        assert_that(real, equal_to(expect))

    def test_delete_flow(self):
        before_delete = self.flow.get_flow_and_tasks()
        self.flow.delete_flow()
        after_delete = self.flow.get_flow_and_tasks()
        assert_that(before_delete, not_(equal_to(after_delete)))

    def teardown_class(self):
        self.flow.driver.quit()
