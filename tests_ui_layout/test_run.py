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
    # page = set_up
   #  #browser = playwright.chromium.launch(headless=False)
   #  #slow motion -> to debug or to demonstrate
   #  browser = playwright.chromium.launch(headless=False, slow_mo=500)
   #  context = browser.new_context()
   #  page = context.new_page()
   #  page.set_default_timeout(15000)
   #  #page.pause()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    # home_page = HomePage(page)
    # expect(home_page.celebrate_header).to_be_visible()
    # expect(home_page.celebrate_body).to_be_visible()

    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.get_by_role("button", name="Log In").click()
        else:
            login_issue = False
        time.sleep(1)
    #page.wait_for_selector("button:has-text(\"Log In\")")
    #page.get_by_role("button", name="Log In").click()
   # page.get_by_role("button", name="Sign up with email").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    #page.get_by_test_id("emailAuth").get_by_label("Email").fill("kaneki@gmail.com")
    # page.fill("[data-testid='siteMembers.container'] >> input[type='email']", "kaneki@gmail.com")
    page.fill("input:below(:text('Email'))", email)
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill(password)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    #page.pause()
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(timeout=5000)
    #
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    page.wait_for_load_state("networkidle")
    # page.wait_for_timeout(timeout=5000)
   #  # locators chaining
   #  product = page.get_by_text("$85").first.locator("xpath=../../../..//p").text_content()
   #  print(product)
   #  # python specific
   #  assert product == 'Shoes'
   #
   #  all_links = page.get_by_role("link").all()
   #  for link in all_links:
   #      if '$85' in link.text_content():
   #          # python specific
   #          assert 'socks' not in link.text_content().lower()
   #          print('Nani nani!!!')
   #
   # # page.get_by_text("©2021 by playwright-practice").click()
   #  page.get_by_role("link", name="Shop Women").nth(0).click()
   #  page.wait_for_timeout(timeout=2000)
   #  page.locator("xpath=//div/wow-image").nth(1).click()
   #  page.wait_for_timeout(timeout=2000)
   #  # playwright specific
   #  expect(page.get_by_text("Home / Shop Women / Shoes")).to_be_visible()
   #  # python specific
   #  assert page.is_visible("text=Home / Shop Women / Shoes")
   #  # better use expect()


    # page.goto("https://github.github.io/clipboard-copy-element/examples/")
    # page.locator("xpath=//clipboard-copy").nth(0).click()
    print('Yamate Kudasai!')
    #
    # # ---------------------
    # context.close()
    # browser.close()


# with sync_playwright() as playwright:
#     test_run(playwright)
