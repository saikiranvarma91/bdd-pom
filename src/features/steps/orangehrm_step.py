from src.app_config import *
from src.pages.orange_login import *

@given('I launched th default browser')
def step_impl(context):
    context.app = AppConfig(context)
    context.obj.load_browser(context)	


@when('I loaded OrangeHRM home page')
def step_impl(context):
    context.browser.maximize_window()
    context.browser.get(context.app.DEFAULT_URL)
    sleep(context.app.DEFAULT_WAIT_TIME)

@when('I filled username "{usr}" and password "{pwd}"')
def step_impl(context,usr,pwd):
    context.obj1 = OrangeLogin(context)
    assert context.obj1.test_fill_username(usr) is True
    assert context.obj1.test_fill_password(pwd) is True

@when('I clicked login button')
def step_impl(context):
    assert context.obj1.test_click_login() is True

@then('I verified whether "{exp_txt}" appears')
def step_impl(context,exp_txt):
    assert context.obj1.test_dashboard(exp_txt) is True   

@then('I logged out from my account')
def step_impl(context):
    assert context.obj1.test_logoff() is True
	
@then('I closed the browser')
def step_impl(context):
    context.obj.unload_browser(context)