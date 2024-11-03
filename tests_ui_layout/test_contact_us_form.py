import time
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
from pom.contact_us_page import ContactUsPage

#to be careful with xfail marker >>> false positive
#@pytest.mark.xfail(reason="submit function not ready")
def test_submit_form(login_set_up):
    page = login_set_up
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("Ken Kaneki","1238 Kobukodzivari Tokyo",
                           "kaneki@gmail.com","890-891-8981",
                           "Jamate Kudasai","I am ghoul")


# with sync_playwright() as playwright:
#     test_submit_form(playwright)
    time.sleep(1)
