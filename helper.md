**List of all expect() assertions**
https://playwright.dev/python/docs/test-assertions

**Layout selectors documentation**
https://playwright.dev/python/docs/other-locators#css-matching-elements-based-on-layout

**Assertions documentation:**
https://playwright.dev/python/docs/test-assertions

**Playwright is a new framework and the POM API**
**is constantly changing. Please check the documentation**
**frequently:**

https://playwright.dev/python/docs/pom

**start**
playwright codegen

**Run all tests**
pytest
or to get more info
pytest -v

 pytest -k test_login --headed
 pytest -k <test name> --headed


# packages/folder : "test*"; Example: "tests_ui_layout"
# python files: "test*"; Example: "test_home_page_layout"
# python functions/modules: "test*" Example: "test_about_us_section_verbiage"
# python classes: "Test*" Example "TestHomePage"

**List of all supported devices**
Registry of all devices:

https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json



https://playwright.dev/python/docs/test-runners

--headed: Run tests in headed mode (default: headless).
--browser: Run tests in a different browser chromium, firefox, or webkit. It can be specified multiple times (default: all browsers).
--browser-channel Browser channel to be used.
--slowmo Run tests with slow mo.
--device Device to be emulated.
--video Whether to record video for each test. on, off, or retain-on-failure (default: off).
--screenshot Whether to automatically capture a screenshot after each test. on, off, or only-on-failure (default: off).
--base-url Specify a base url

pytest --headed --slowmo=400 --device="iPhone 11" --video=retain-on-failure --output=JamateKudasai