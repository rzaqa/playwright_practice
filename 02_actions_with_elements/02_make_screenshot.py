# Quick way to make a screenshot  and save as a file
page.screenshot(path="screenshot.png")
page.screenshot(path="screen/screenshot.png")

# Make a screenshot of the whole page
page.screenshot(path="screenshot.png", full_page=True)

# A screenshot of a web element
page.locator(".header").screenshot(path="screenshot.png")

# Chose a format og image - "jpeg" or "png"
page.screenshot(path="example.jpeg", type="jpeg")

#Chose a quality for an image. from 0 to 100
page.screenshot(path="example.jpeg", type="jpeg", quality=80)

#Chose an area of the window
page.screenshot(path="clipped_image.png", clip={"x": 50, "y": 0, "width": 400, "height": 300})

# Remove background on an image
page.screenshot(path="transparent_background.png", omit_background=True)

# Set a timeout before making a screenshot
page.screenshot(path="timeout_example.png", timeout=10000)





