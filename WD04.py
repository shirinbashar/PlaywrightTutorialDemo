# Open Modal, perform action inside modal, close modal -> ensure state resets

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://webdriveruniversity.com/index.html")
    expect(page.get_by_role("link", name="DATEPICKER Datepicker What")).to_be_visible()

    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="POPUP & ALERTS Close those").click()
    page1 = page1_info.value
    expect(page1.get_by_role("link", name="WebdriverUniversity.com (")).to_be_visible()

    page1.locator("#button2").get_by_text("CLICK ME!").click()
    expect(page1.get_by_role("button", name="×")).to_be_visible()

    page1.get_by_role("button", name="Close").click()
    expect(page1.get_by_role("heading", name="Annoying Popup & Alerts!")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

