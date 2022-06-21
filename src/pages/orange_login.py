from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from time import sleep

class OrangeLogin:
	def __init__(self,context):
		self.context = context
	
	def test_fill_username(self,usr):
		self.context.browser.find_element(By.ID,"txtUsername").send_keys(usr)
		return True

	def test_fill_password(self,pwd):
		self.context.browser.find_element(By.ID,"txtPassword").send_keys(pwd)
		return True

	def test_click_login(self):
		self.context.browser.find_element(By.ID,"btnLogin").click()
		sleep(self.context.app.DEFAULT_WAIT_TIME)
		return True

	def test_dashboard(self,exp_txt):
		status = True
		try:
        		element = self.context.browser.find_element(By.XPATH,"//div[@class='head']//h1")
        		rndrd_txt = element.text
        		assert rndrd_txt==exp_txt, "Failed to load dashboard page."
		except (NoSuchElementException,Exception):
			status = False
		return status

	def test_logoff(self):
		status = True
		try:
        		self.context.browser.find_element(By.ID,"welcome").click()
        		sleep(self.context.app.DEFAULT_WAIT_TIME)
        		self.context.browser.find_element(By.LINK_TEXT,"Logout").click()
        		sleep(self.context.app.DEFAULT_WAIT_TIME)
		except:
			status = False
		return status