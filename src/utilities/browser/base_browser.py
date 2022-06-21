from abc import *
class BaseBrowser(ABC):
	'''
	BaseBrowser is an interface contains two abstract methods
	used to define structure of methods which should be same
	for any browser class which is sub class of this BaseBrowser.
	Note: Advantage of this style of implementation is in future
	      if any new browser comes we just need to implement a
	      new class that is subclass of BaseBrowser.	
	'''
	
	def load_browser(self):
		'''
		This method should be implemented in the subclass of BaseBrowser.
		That should load selenium webdriver and browser drivers.
		'''	
		pass

	def unload_browser(self):
		'''
		This method should be implemented in the subclass of BaseBrowser.
		That should close & quit the browser.
		'''
		pass