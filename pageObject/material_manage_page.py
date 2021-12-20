import time
from selenium.webdriver.common.by import By
from pageObject.base_page import BasePage
from utils.mock import Mock


class MaterialManagePage(BasePage):
    _base_url = "https://comba-test.teletraan.io/subapp/plm/base/material"

    # 创建物料时，新增表单中根据物料属性不同，物料类型提供options不同；根据传入参数选取第n个属性，然后返回所有类别options
    def create_material_form_get_category(self, pick_num_material_form: int):
        self.driver.find_element(By.XPATH, '//button[span="新增物料"]').click()
        self.driver.find_element(By.XPATH,
                                 '//div[label="*物料名称"]/ancestor::div//input[@name="property"]').click()  # 物料属性
        self.driver.find_element(By.XPATH,
                                 f'//div[@class="MuiAutocomplete-popper"]//li[{pick_num_material_form}]').click()
        self.driver.find_element(By.XPATH, '//div[label="*物料名称"]/ancestor::div//input[@name="category"]').click()

        options = [i.text for i in self.driver.find_elements(By.XPATH, '//div[@class="MuiAutocomplete-popper"]//li')]
        self.driver.find_element(By.XPATH, '//button[span="取消"]').click()
        return options

    def create_material_get_name(self):
        mock = Mock()
        material_name = mock.mock_data("name")  # 名称
        material_code = mock.mock_data("code")  # 编号
        material_version = mock.mock_data("version")  # 版本
        material_unit = mock.mock_data("unit")  # 计量单位
        self.driver.find_element(By.XPATH, '//button[span="新增物料"]').click()
        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(material_name)
        self.driver.find_element(By.XPATH, '//input[@name="code"]').send_keys(material_code)
        self.driver.find_element(By.XPATH, '//input[@name="versions"]').send_keys(material_version)
        self.driver.find_element(By.XPATH, '//input[@name="unit"]').send_keys(material_unit)
        self.driver.find_element(By.XPATH,
                                 '//div[label="*物料名称"]/ancestor::div//input[@name="property"]').click()  # 物料属性
        self.driver.find_element(By.XPATH, '//div[@class="MuiAutocomplete-popper"]//li[1]').click()
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        time.sleep(3)
        return material_name

    # 查询返回第一行数据第n个column的value
    def get_material_n_column_value(self, n: int):
        get_material_column_ele = self.driver.find_element(By.XPATH, f'//tr[1]/td[{n}]')
        get_material_column_value = get_material_column_ele.text
        return get_material_column_value

    # 更新第一个物料的指定字段，传入参数就是它滴英文名
    def update_material_get_name(self, column: str):
        mock = Mock()
        material_column = mock.mock_data(column)  # 名称
        self.driver.find_element(By.XPATH, '//tbody/tr[1]//button[@title="查看详情"]').click()
        # 要义：碰到奇怪的等一秒，不要随便删；这里的状况是如果不等，打开这个表单后字段内容都不会预填充，导致无法编辑成功
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//button[span="编辑物料"]').click()
        clear_ele = self.driver.find_element(By.XPATH, f'//input[@name="{column}"]')
        self.new_clear(clear_ele)
        self.driver.find_element(By.XPATH, f'//input[@name="{column}"]').send_keys(material_column)
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        return material_column

    def delete_material(self):
        self.driver.find_element(By.XPATH, '//tbody/tr[1]//button[@title="删除"]').click()
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        time.sleep(3)
