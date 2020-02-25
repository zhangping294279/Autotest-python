#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :  add_img_to_report.py
@Contact :  zhangping294279@163.com
@MTime :    2020/2/26 1:38 AM
@Author:    zhangping
@Desciption: None
'''
from selenium import webdriver
import unittest

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        # self.driver = webdriver.Chrome()
        self.imgs = []
        self.addCleanup(self.cleanup)

    # def tearDown(self):
    #     self.driver.quit()

    def cleanup(self):
        pass

    def test_case1(self):
        """ 百度搜索"""
        print("测试"*10)
        self.driver.get("https://www.baidu.com")
        self.add_img()
        self.driver.find_element_by_id('kw').send_keys(u'百度一下')
        self.add_img()
        self.driver.find_element_by_id('su').click()
        # time.sleep(1)
        self.add_img()
        # self.assertTrue(False)

    def test_case2(self):
        """163邮箱"""
        self.driver.get("https://mail.163.com/")
        # raise TypeError
        # self.assertTrue(False)

    def test_case3(self):
        """ 博客园"""
        self.driver.get("https://blog.csdn.net/qw943571775")
        self.imgs.append(self.driver.get_screenshot_as_base64())
        # raise TypeError

    def test_case4(self):
        u""" 淘宝"""
        self.driver.get("http://www.taobao.com/")
        self.add_img()
        # self.assertTrue(True)
        # raise TypeError

    def test_case5(self):
        u""" testerhome"""
        self.driver.get("http://testerhome.com/")
        self.add_img()
        # raise TypeError
        # self.assertTrue(False)