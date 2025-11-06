#Submit invalid email -> expect validation error
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://webdriveruniversity.com/index.html")
    expect(page.get_by_role("link", name="DATEPICKER Datepicker What")).to_be_visible()

    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="CONTACT US Contact Us Form").click()
    page1 = page1_info.value
    expect(page1.get_by_role("link", name="WebdriverUniversity.com (New")).to_be_visible()

    page1.get_by_role("textbox", name="Email Address").click()
    page1.get_by_role("textbox", name="Email Address").fill("tdbank#gmx")
    page1.get_by_role("button", name="SUBMIT").click()

    # Assert that the error message is visible
    expect(page1.get_by_text("Error: Invalid email address")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
