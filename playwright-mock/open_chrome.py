from playwright.sync_api import sync_playwright

def open_chrome():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        page.wait_for_timeout(5000)  # Keep the browser open for 5 seconds
        browser.close()

if __name__ == "__main__":
    open_chrome()
