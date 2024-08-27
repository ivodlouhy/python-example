from playwright.sync_api import Page


def test_polling(page: Page):
    page.goto("http://localhost:8000/timeout-3s.html")
    button_locator = page.locator('button').filter(has_text='Button')
    assert button_locator.is_visible() == True, "Expected button to be visible"
