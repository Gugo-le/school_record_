from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch()
page = browser.new_page()
page.goto("https://google.com")
page.screenshot(path = "screenshot.png")

# 왜 에러 남?
