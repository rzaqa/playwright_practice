from playwright.sync_api import Playwright, sync_playwright

def test_loc(page):
    page.goto('https://zimaev.github.io/text_input/')
    page.get_by_label("Email address").fill("qa@example.com")
    page.get_by_title("username").fill("Anton")
    page.get_by_placeholder('password').fill("secret")
    page.get_by_role('checkbox').click()

def test_or(page):
    selector = page.locator("input").or_(page.locator("text"))
    selector.fill("Hello Stepik")

def test_locator_and(page):
    page.goto("https://zimaev.github.io/locatorand/")
    selector = page.get_by_role("button", name="Sing up").and_(page.get_by_title("Sing up today"))
    selector.click()


"""
Other locators

---------------------------------------------------------------------------------------------------------
Chain of locators:
page.locator("#navbarNavDropdown >> li:has-text('Company')").click()
---------------------------------------------------------------------------------------------------------
Filters:
page.locator("li").filter(has_text='Company').click()
page.locator('li').filter(has=page.locator('.dropdown-toggle')).click()
---------------------------------------------------------------------------------------------------------
Using HAS NOT:
page.goto("https://zimaev.github.io/filter/")
row_locator = page.locator("tr")
row_locator.filter(has_not=page.get_by_role("button")).count()

OR

page.goto("https://zimaev.github.io/filter/")
row_locator = page.locator("tr")
row_locator.filter(has_not_text="helicopter").
---------------------------------------------------------------------------------------------------------



page.get_by_role("button").count()
page.get_by_role("listitem").nth(1)

---------------------------------------------------------------------------------------------------------
page.goto('https://zimaev.github.io/checks-radios/')
checkbox = page.locator("input")
for i in range(checkbox.count()):
    checkbox.nth(i).click()
    
    OR 
page.goto('https://zimaev.github.io/checks-radios/')
checkboxes = page.locator("input")
for checkbox in checkboxes.all():
    checkbox.check()
---------------------------------------------------------------------------------------------------------




"""

