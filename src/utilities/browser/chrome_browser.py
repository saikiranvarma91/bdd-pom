from src.utilities.browser.base_browser import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ChromeBrowser(BaseBrowser):
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
			path = ChromeDriverManager(path="./src/browser_drivers/chrome").install()
			chrome_service = ChromeService(executable_path=path)
			context.browser = webdriver.Chrome(service=chrome_service)
		else:
			path = "./src/browser_drivers/default/chromedriver.exe"
			chrome_service = ChromeService(executable_path=path)
			context.browser = webdriver.Chrome(service=chrome_service)

	def unload_browser(self,context):
		'''
		Here we will close and quit opened browser
		'''
		context.browser.close()
		context.browser.quit()

	