from playwright.sync_api import Page, expect
class HRMAddEmployeePage:
    def __init__(self, page: Page):
        self.page = page
        
    def add_employee (self):
        self.page.get_by_role("link", name="PIM").click()
        self.page.get_by_role("link", name="Add Employee").click()
        self.page.get_by_role("textbox", name="First Name").fill("B")
        self.page.get_by_role("textbox", name="Middle Name").fill("G")
        self.page.get_by_role("textbox", name="Last Name").fill("N")
        self.page.locator(".oxd-switch-input").click()
        self.page.get_by_role("textbox").nth(5).fill("Gajera")
        self.page.locator("input[type=\"password\"]").first.fill("admin123")
        self.page.locator("input[type=\"password\"]").nth(1).fill("admin123")
        self.page.get_by_role("button", name="Save").click()
        try:
            self.page.get_by_text("Username already exists").wait_for(timeout=2000)
            print("⚠ Username already exists → deleting old employee...")
            self.delete_employee()
            self.add_employee()
        except TimeoutError:
            expect(self.page.get_by_text("SuccessSuccessfully Saved×")).to_be_visible()

    def delete_employee(self):
        self.page.get_by_role("link", name="PIM").click()
        expect(self.page.get_by_role("heading", name="Employee Information")).to_be_visible()
        self.page.get_by_role("textbox", name="Type for hints...").first.fill("b g n")
        self.page.get_by_role("option", name="B G N").first.click()
        self.page.get_by_role("button", name="Search").click()
        expect(self.page.get_by_text("B G")).to_be_visible()
        self.page.get_by_role("cell", name="").click()
        self.page.get_by_role("button", name=" Delete Selected").click()
        self.page.get_by_role("button", name=" Yes, Delete").click()
        expect(self.page.get_by_text("SuccessSuccessfully Deleted×")).to_be_visible()
        
        
        