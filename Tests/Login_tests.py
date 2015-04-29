#!/usr/bin/python

from appium import webdriver 
import time
import unittest
import os

class LoginTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['appium-version'] = '1.0'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['app'] = os.path.abspath('/Users/mkim/Documents/AUT/app/build/outputs/apk/app-debug-unaligned.apk')

        self.wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        self.wd.implicitly_wait(60)

    def tearDown(self):
        self.wd.quit()

    def test_success(self):
        basepath = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/"
        basepath2 = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/"
	self.wd.find_element_by_xpath(basepath + "android.widget.EditText[1]").send_keys("success@envato.com")
	self.wd.find_element_by_xpath(basepath + "android.widget.EditText[2]").send_keys("password")
	self.wd.find_element_by_xpath(basepath + "android.widget.Button[1]").click()
        try:
	    self.wd.find_element_by_xpath(basepath2 + "android.widget.TextView[1]")
        except: 
            self.fail("Not at Login Success page.\n")

	self.wd.find_element_by_xpath(basepath2 + "android.widget.Button[1]").click()
         
    def test_fail(self):
        basepath = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/"
	self.wd.find_element_by_xpath(basepath + "android.widget.EditText[1]").send_keys("success@envato.com")
	self.wd.find_element_by_xpath(basepath + "android.widget.EditText[2]").send_keys("wrongpassword")
	self.wd.find_element_by_xpath(basepath + "android.widget.Button[1]").click()
        try:
	    self.wd.find_element_by_xpath(basepath + "android.widget.Button[1]")
        except:
            self.fail("Not still at login screen.\n")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
