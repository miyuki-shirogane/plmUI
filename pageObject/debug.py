# -*-coding:utf-8 -*-

"""
# File       : debug
# Time       ：2021/12/15 4:49 下午
# Author     ：10
"""
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from seletools.actions import drag_and_drop
from selenium.webdriver.common.by import By


from utils.mock import Mock


def get_driver(port=8888):
    """拿到打开的浏览器，debug模式，调试用"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:%s" % port)
    c = webdriver.Chrome(port=19888, options=options)
    return c


def Clear(element):
    """清空输入框内容，部分使用clear没有用，使用这种方法可以"""
    element.clear()
    element.send_keys(Keys.ARROW_DOWN)
    while element.get_attribute("value"):
        element.send_keys(Keys.BACKSPACE)


def add_task(add_num: int):
    driver = get_driver()
    for task_num in range(1, add_num + 1):
        driver.find_element(By.XPATH,
                            f'//label[contains(text(),"任务{task_num}名称")]/parent::div/parent::div'
                            '/following-sibling::div//button[2]').click()


def input_task_name(*args):
    driver = get_driver()
    mock = Mock()
    tmp_list = []
    for (task_name_suffix, n) in args:
        task_name = mock.mock_data("task_name_" + chr(task_name_suffix))
        driver.find_element(By.XPATH, f'//input[@name="taskConfiguration.{n}.name"]').send_keys(task_name)
        tmp_list.append(task_name)
    return tmp_list


def test():
    driver = get_driver()
    mock = Mock()
    flow_name = mock.mock_data("flow_name")
    res = [flow_name]
    driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(flow_name)
    add_task(add_num=2)
    first_add = input_task_name((ord("b"), 0), (ord("d"), 1), (ord("a"), 2))
    res.extend(first_add)
    add_task(2)
    second_add = input_task_name((ord("c"), 1), (ord("e"), 2))
    res[2:len(res) - 2] = second_add
    driver.find_element(By.XPATH,
                        '//label[contains(text(),"任务3名称")]/parent::div/parent::div/following-sibling::div//button[1]').click()
    res.pop(3)
    print(res)


def test_1():
    driver = get_driver()
    path1 = driver.find_element(By.XPATH, '//p[contains(text(),"设定任务")]/following-sibling::div[1]/div')
    path2 = driver.find_element(By.XPATH, '//p[contains(text(),"设定任务")]/following-sibling::div[2]/div')
    drag_and_drop(driver, path1, path2)

