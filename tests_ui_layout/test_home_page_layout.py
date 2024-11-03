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


@pytest.mark.skip(reason="not ready")
def test_headers(login_set_up) -> None:
    page = login_set_up
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()

    print('\nYamate Kudasai!')

