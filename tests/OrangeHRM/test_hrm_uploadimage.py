"""
login to hrm site
go to PIM
click on add button
click on upload image + button
select image
save record with details.
varify image is displaying
delete saved record.

"""
import re
from playwright.sync_api import Page, expect
from Pages.OrangeHRM_pages.hrm_login import HRMLoginPage
from Pages.OrangeHRM_pages.hrm_add_employee import HRMUploadimagePage

def test_hrm_upload_image(page: Page) -> None:
    
    login = HRMLoginPage(page)
    addemployee = HRMUploadimagePage(page)
    deleteemployee = HRMUploadimagePage(page)
    
    login.login()
    
    addemployee.add_employee()
    page.get_by_role("heading", name="Bri Nar").wait_for(state="visible")
    expect(page.get_by_role("heading", name="Bri Nar")).to_be_visible
    deleteemployee.delete_employee()