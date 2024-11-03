import time

from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
import pytest


#custom markers -> to run specific mark: pytest -m smoke
#possibility to nest markers
# @pytest.mark.smoke
# @pytest.mark.sanity
# @pytest.mark.parametrize("email, password", [("kaneki@gmail.com", "Kaneki1"),
#                                              pytest.param("jonatan.joster@gmail.com", "jojo123", marks=pytest.mark.xfail),
#                                              pytest.param("kaneki@gmail", "Kaneki1", marks=pytest.mark.xfail)])

@pytest.mark.parametrize("email", ["kaneki@gmail.com",
                                   pytest.param("jonatan.joster@gmail.com", marks=pytest.mark.xfail),
                                   pytest.param("kaneki@gmail", marks=pytest.mark.xfail)])

@pytest.mark.parametrize("password", ["Kaneki1",
                                      pytest.param("jojo123", marks=pytest.mark.xfail),
                                      "Kaneki1"])
def test_run(page, email, password) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    time.sleep(2)
    page.wait_for_timeout(timeout=5000)
    #page.wait_for_load_state("networkidle")

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

    page.fill("input:below(:text('Email'))", email)
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill(password)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_timeout(timeout=2000)
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    expect(page.locator("[aria-label=\"kaneki account menu\"]")).to_be_visible()
    print('Yamate Kudasai!')
