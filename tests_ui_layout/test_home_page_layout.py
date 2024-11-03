import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage


@pytest.mark.sanity
def test_about_us_section_verbiage(login_set_up) -> None:
    #Assess - Given
    page = login_set_up

    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()

    print('\nYamate Kudasai!')

    # ---------------------
    # context.close()
    # browser.close()


@pytest.mark.skip(reason="not ready")
def test_headers(login_set_up) -> None:
    # #Assess - Given
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # #Open new page
    # page = context.new_page()
    # page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.set_default_timeout(3000)
    page = login_set_up
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()

    print('\nYamate Kudasai!')

    # # ---------------------
    # context.close()
    # browser.close()
# with sync_playwright() as playwright:
#     test_about_us_section_verbiage(playwright)
