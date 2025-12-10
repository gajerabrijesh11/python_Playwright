import re
from playwright.sync_api import Page, expect

from Pages.OrangeHRM_pages.hrm_login import HRMLoginPage
from Pages.OrangeHRM_pages.hrm_site_open import HRMSiteOpenPage


def test_hrm_login(page: Page) -> None:
    
    opensite = HRMSiteOpenPage(page)
    login = HRMLoginPage(page)
    opensite.open_site()
    login.click_login()
    expect(page).to_have_title("OrangeHRM")