import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.get_by_test_id("handle-button").click()
    page.get_by_test_id("signUp.switchToSignUp").wait_for(state="visible")
    page.get_by_test_id("signUp.switchToSignUp").click(timeout=60000)
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("qagregg2021@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Ari1987umi$")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    print("Yay")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
