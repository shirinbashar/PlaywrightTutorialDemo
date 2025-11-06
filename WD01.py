# Validate Contact Us form submission
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://webdriveruniversity.com/index.html")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="CONTACT US Contact Us Form").click()
    page1 = page1_info.value
    page1.get_by_role("textbox", name="First Name").click()
    page1.get_by_role("textbox", name="First Name").fill("QA")
    page1.get_by_role("textbox", name="Last Name").click()
    page1.get_by_role("textbox", name="Last Name").fill("Shuruq")
    page1.get_by_role("textbox", name="Email Address").click()
    page1.get_by_role("textbox", name="Email Address").fill("qagregg2021@gmail.com")
    page1.get_by_role("textbox", name="Comments").click()
    page1.get_by_role("textbox", name="Comments").fill("testing testing testing")
    page1.get_by_role("button", name="SUBMIT").click()
    expect(page1.get_by_role("heading")).to_have_text("Thank You for your Message!")

    print("Test Successful")


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
