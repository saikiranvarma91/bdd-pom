from src.utilities.browser.base_browser import *
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import os

class FirefoxBrowser(BaseBrowser):
	'''
	This class should implement definition of all 
	abstract methods of BaseBrowser
	'''

	def load_browser(self,context):
		'''
		Here we will load selenium webdriver and
		create browser object using chrome driver 
		'''
		if context.app.DRIVER_MANAGER_STATUS:
			os.environ['GH_TOKEN'] = context.app.FIREFOX_TOKEN
			path = GeckoDriverManager(path="./src/browser_drivers/firefox").install()
			firefox_service = FirefoxService(executable_path=path)
			context.browser = webdriver.Firefox(service=firefox_service)
		else:
			path = "./src/browser_drivers/default/geckodriver.exe"
			firefox_service = FirefoxService(executable_path=path)
			context.browser = webdriver.Firefox(service=firefox_service)

	def unload_browser(self,context):
		'''
		Here we will close and quit opened browser
		'''
		context.browser.close()
		context.browser.quit()

	