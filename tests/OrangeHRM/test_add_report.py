# this test is for to add report in PIM module.

import re
from playwright.sync_api import Page, expect
from Pages.OrangeHRM_pages.hrm_login import HRMLoginPage


def test_add_report(page: Page) -> None:
    login = HRMLoginPage(page)
    login.login()
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("link", name="Reports").click()
    page.get_by_role("button", name=" Add").click()
    page.get_by_role("textbox", name="Type here").click()
    page.pause()
    page.get_by_role("textbox", name="Type here").fill("test report brijesh")
    page.locator(".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow").first.click()
    page.get_by_text("Employee Name").click()
    page.locator("div:nth-child(5) > .oxd-grid-4 > div > .oxd-input-group > div:nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon").first.click()
    page.get_by_text("Personal").click()
    page.locator("div:nth-child(5) > .oxd-grid-4 > .oxd-grid-item.oxd-grid-item--gutters.orangehrm-report-criteria > .oxd-input-group.oxd-input-field-bottom-space > div:nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon").click()
    page.get_by_text("Employee First Name").click()
    page.get_by_role("button", name="").nth(1).click()
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_role("heading", name="test report brijesh")).to_be_visible()
