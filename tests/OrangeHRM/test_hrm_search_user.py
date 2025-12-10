import re
from playwright.sync_api import Page, expect
from Pages.OrangeHRM_pages.hrm_search_user import HRMSystemUserPage
from Pages.OrangeHRM_pages.hrm_login import HRMLoginPage
# from Pages.OrangeHRM_pages.hrm_site_open import HRMSiteOpenPage

def test_hrm_search_user(page: Page) -> None:
    # opensite =HRMSiteOpenPage(page)
    login = HRMLoginPage(page)
    search_user = HRMSystemUserPage(page)
    # opensite.open_site()
    # login.enter_username("Admin")
    # login.enter_password("admin123")
    login.login()
    search_user.search_user()
    expect(page.get_by_text("Records Found")).to_be_visible()
    
