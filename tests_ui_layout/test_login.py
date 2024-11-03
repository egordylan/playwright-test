from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
import pytest


#custom markers -> to run specific mark: pytest -m smoke
#possibility to nest markers
@pytest.mark.smoke
@pytest.mark.sanity
def test_login(login_set_up) -> None:
    page = login_set_up

    page.wait_for_timeout(timeout=2000)
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()

    # locators chaining
    product = page.get_by_text("$85").first.locator("xpath=../../../..//p").text_content()
    print(product)

    # python specific
    assert product == 'Shoes'

    all_links = page.get_by_role("link").all()
    for link in all_links:
        if '$85' in link.text_content():
            # python specific
            assert 'socks' not in link.text_content().lower()
            print('Nani nani!!!')

    page.get_by_role("link", name="Shop Women").nth(0).click()
    page.wait_for_timeout(timeout=2000)
    page.locator("xpath=//div/wow-image").nth(1).click()
    page.wait_for_timeout(timeout=2000)
    # playwright specific >>> better use expect() than assert
    expect(page.get_by_text("Home / Shop Women / Shoes")).to_be_visible()
    # python specific
    assert page.is_visible("text=Home / Shop Women / Shoes")

    print('Yamate Kudasai!')
