from playwright.sync_api import Page
from config.config import Config
class HRMLoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login (self):
        self.page.goto(Config.BASE_URL)
        self.page.get_by_role("textbox", name="Username").fill(Config.USERNAME)
        self.page.get_by_role("textbox", name="Password").fill(Config.PASSWORD)
        self.page.get_by_role("button", name="Login").click()



        """""
        self.hrmuser_input = page.get_by_role("textbox", name="Username")
        self.hrmpassword_input = page.get_by_role("textbox", name="Password")
        self.hrmlogin_button = page.get_by_role("button", name="Login")
    def enter_username (self, username):
        self.hrmuser_input.fill(username)
        
    def enter_password (self, password):
        self.hrmpassword_input.fill(password)
        
    def click_login (self):
        self.hrmlogin_button.click()
"""""