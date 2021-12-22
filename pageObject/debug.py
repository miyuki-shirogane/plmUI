# -*-coding:utf-8 -*-

"""
# File       : debug
# Time       ：2021/12/15 4:49 下午
# Author     ：10
"""
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


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


def test(name = "新品定制"):
    driver = get_driver()
    ele = driver.find_element(By.XPATH, '//label[contains(text(),"立项文档")]/parent::div//input')
    ele.send_keys("/Users/yilin/desktop/hayasaka.jpeg")