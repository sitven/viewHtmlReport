#!/usr/bin/python3.6
# coding=utf-8
# Author: Sitven


import time
import os
import unittest
from selenium import webdriver
from common.globalparam import img_path
from common.log import Log


class Test(unittest.TestCase):
    """测试-百度搜索"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        Log().info(" 打开谷歌浏览器")

    def tearDown(self):
        self.driver.quit()
        Log().info(" 关闭谷歌浏览器")

    def test_001(self):
        """百度搜索_Python"""
        try:
            self.driver.maximize_window()
            Log().info(" 浏览器窗口最大化")
            self.driver.implicitly_wait(time_to_wait=5)
            Log().info(" 设置隐性等待时间为5秒")
            self.driver.get(url="https://www.baidu.com")
            Log().info(" 访问百度")
            self.driver.find_element_by_xpath("//input[@id='kw']").send_keys("Python")
            Log().info(" 搜索输入框输入Python")
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@id='su']").click()
            Log().info(" 点击百度一下搜索框")
            time.sleep(1)
            title = self.driver.title
            Log().info(" 获得当前页面标题：%s" % title)
            time.sleep(2)
            assert "百度一下", title
        except Exception as e:
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            self.driver.get_screenshot_as_file(img_name)
            Log().info(message="异常截图名称：%s" % os.path.split(img_name)[1])
            raise

    def test_002(self):
        """百度搜索_Appium"""
        """百度搜索_Python"""
        try:
            self.driver.maximize_window()
            Log().info(" 浏览器窗口最大化")
            self.driver.implicitly_wait(time_to_wait=5)
            Log().info(" 设置隐性等待时间为5秒")
            self.driver.get(url="https://www.baidu.com")
            Log().info(" 访问百度")
            self.driver.find_element_by_xpath("//input[@id='kw']").send_keys("Appium")
            Log().info(" 搜索输入框输入Python")
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@id='su']").click()
            Log().info(" 点击百度一下搜索框")
            time.sleep(1)
            title = self.driver.title
            Log().info(" 获得当前页面标题：%s" % title)
            time.sleep(2)
            assert "Appium_百度搜索", title
        except Exception as e:
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" 异常截图保存路径: %s  异常截图名称：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            raise


if __name__ == "__main__":
    unittest.main()
