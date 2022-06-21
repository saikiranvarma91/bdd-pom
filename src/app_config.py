from behave import *
from src.utilities.browser.chrome_browser import *
from src.utilities.browser.firefox_browser import *
from time import sleep
import pyfiglet as pyg  

class AppConfig:
	PROJECT_NAME		= "B E H A V E"
	DEFAULT_BROWSER 	= ChromeBrowser()
	DRIVER_MANAGER_STATUS 	= False
	FIREFOX_TOKEN		= "token_here"
	DEFAULT_URL 		= "https://opensource-demo.orangehrmlive.com/"
	DEFAULT_WAIT_TIME 	= 3
	DEFAULT_WEB_WAIT_TIME	= 10
	
	def __init__(self,context):
		context.obj = self.DEFAULT_BROWSER  
		res= pyg.figlet_format(self.PROJECT_NAME)
		print(res) 
		
