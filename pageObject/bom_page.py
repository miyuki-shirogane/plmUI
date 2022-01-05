from pageObject.base_page import BasePage
from utils.env import Environment


class BOMPage(BasePage):
    env = Environment()
    _base_url = env.url(module="bom")
