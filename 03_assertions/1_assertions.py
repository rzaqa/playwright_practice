from playwright.sync_api import Page, expect

# Just steps without checks
def test_add_todo(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.locator("h2").is_visible()

# Test with assert
def test_add_todo_assert(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    assert page.locator("h2").is_visible()

# Test with expect
def test_add_todo_expect(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page.locator('h2')).to_be_visible()
