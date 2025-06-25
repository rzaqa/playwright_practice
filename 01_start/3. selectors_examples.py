from playwright.sync_api import Playwright, sync_playwright, expect


# New version of test using a page fixture


def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")

"""
1. Search by ID: 
CSS: page.locator("#new-todo").click()
XPAth: page.locator("//*[@id='new-todo']").click()

2. Search by class
CSS: page.locator(".new-todo").click()
XPAth: page.locator("//*[@class='new-todo']").click()

3. Search by several classes
CSS: page.locator(".new-todo").click()
XPAth: page.locator("//*[@class='new-todo']").click()


"""

