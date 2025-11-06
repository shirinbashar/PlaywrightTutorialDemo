#To-Do List: Add, Complete, Delete
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://webdriveruniversity.com/index.html")
    expect(page.get_by_role("link", name="DATEPICKER Datepicker What")).to_be_visible()

    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="TO DO LIST Task1 [ ] - Task2").click()
    page1 = page1_info.value
    expect(page1.get_by_role("heading", name="TO-DO LIST")).to_be_visible()

    page1.get_by_role("textbox", name="Add new todo").click()
    page1.get_by_role("textbox", name="Add new todo").fill("Water bottle")
    page1.get_by_role("textbox", name="Add new todo").click()
    page1.get_by_role("textbox", name="Add new todo").press("Enter")
    page1.get_by_role("textbox", name="Add new todo").fill("Buy plastic")
    page1.get_by_role("textbox", name="Add new todo").press("Enter")
    page1.get_by_role("textbox", name="Add new todo").fill("buy groceries")
    page1.get_by_role("textbox", name="Add new todo").press("Enter")
    page1.locator("#plus-icon").click(button="right")
    page1.locator("#plus-icon").click()
    page1.get_by_role("listitem").filter(has_text="Water bottle").locator("i").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
