# Get text from an element:

element = page.locator('a:has-text("playwright")')
print(element.inner_text())

element = page.locator('a:has-text("playwright")')
print(element.text_content())

# Get a list of all texts
page.goto('https://zimaev.github.io/table/')
row = page.locator("tr")
print(row.all_inner_texts())

page.goto('https://zimaev.github.io/table/')
row = page.locator("tr")
print(row.all_text_contents())

# To get an HTML-code of an element
element = page.locator('a:has-text("playwright")')
print(element.inner_html())

