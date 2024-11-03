import time
from playwright.sync_api import Playwright, expect
import pytest


# @pytest.fixture(scope="session")
# def set_up(browser):
#     #Assess - Given
#     # browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     context = browser.new_context()
#     #Open new page
#     page = context.new_page()
#     page.goto("https://symonstorozhenko.wixsite.com/website-1")
#     page.set_default_timeout(3000)
#
#     yield page
#     page.close()


@pytest.fixture
def set_up(page):
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    page.wait_for_load_state("networkidle")

    yield page


# @pytest.fixture(scope="session")
@pytest.fixture
def login_set_up(set_up):
    page = set_up
    page.wait_for_load_state("networkidle")

    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.get_by_role("button", name="Log In").click()
        else:
            login_issue = False
        time.sleep(1)

    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    # page.get_by_test_id("emailAuth").get_by_label("Email").fill("kaneki@gmail.com")
    # page.fill("[data-testid='siteMembers.container'] >> input[type='email']", "kaneki@gmail.com")
    page.fill("input:below(:text('Email'))", "kaneki@gmail.com")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill("Kaneki1")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_load_state("networkidle")

    yield page

