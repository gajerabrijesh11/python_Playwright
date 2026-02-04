from playwright.sync_api import Page, expect
class HRMAddREPORTPage:
    def __init__(self, page: Page):
        self.page = page
        
    def add_report (self):
        self.page.get_by_role("link", name="PIM").click()
        self.page.get_by_role("link", name="Reports").click()
        self.page.get_by_role("button", name=" Add").click()
        self.page.get_by_role("textbox", name="Type here").click()
        self.page.get_by_role("textbox", name="Type here").fill("test report brijesh")
        self.page.locator(".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow").first.click()
        self.page.get_by_text("Employee Name").click()
        self.page.locator("div:nth-child(5) > .oxd-grid-4 > div > .oxd-input-group > div:nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon").first.click()
        self.page.get_by_text("Personal").click()
        self.page.locator("div:nth-child(5) > .oxd-grid-4 > .oxd-grid-item.oxd-grid-item--gutters.orangehrm-report-criteria > .oxd-input-group.oxd-input-field-bottom-space > div:nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon").click()
        self.page.get_by_text("Employee First Name").click()
        self.page.get_by_role("button", name="").nth(1).click()
        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_role("heading", name="test report brijesh")).to_be_visible()

    def delete_report (self):
        self.page.get_by_role("link", name="PIM").click()
        self.page.get_by_role("link", name="Reports").click()
        self.page.get_by_role("textbox", name="Type for hints...").fill("test")
        self.page.get_by_role("option").get_by_text("test report brijesh").click()
        self.page.get_by_role("button", name="Search").click()
        self.page.locator(".oxd-table-card-cell-checkbox > .oxd-checkbox-wrapper > label > .oxd-checkbox-input > .oxd-icon").click()
        self.page.get_by_role("button", name=" Delete Selected").click()
        self.page.get_by_role("button", name=" Yes, Delete").click()
        expect(self.page.get_by_text("SuccessSuccessfully Deleted")).to_be_visible()
