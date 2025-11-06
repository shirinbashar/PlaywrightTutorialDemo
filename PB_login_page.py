#Parabank Login Page
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://parabank.parasoft.com/parabank/index.htm;jsessionid=A2CAFFA830BAC42EE3A3D1193C05B478")
    expect(page.get_by_role("img", name="ParaBank")).to_be_visible()

    page.locator("input[name=\"username\"]").click()
    page.locator("input[name=\"username\"]").fill("qa_gregg2021")
    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill("1234")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("row", name="$515.50 $515.50")).to_be_visible()

    expect(page.get_by_role("heading", name="Accounts Overview")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
