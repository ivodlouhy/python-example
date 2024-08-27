import time

import polling
import pytest
import logging

from playwright.sync_api import Page, expect

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def test_assert_is_visible_no_wait(page: Page):

    # Fails → Locator.is_visible() doesn't wait
    # See: https://playwright.dev/python/docs/api/class-locator#locator-is-visible

    page.goto("http://localhost:8000/timeout-3s.html")
    button_locator = page.locator('button').filter(has_text='Button')
    assert button_locator.is_visible() == True, "Expected button to be visible"


def test_assert_is_visible_wait_sleep(page: Page):

    # Passes → Wait using time.sleep is not a good practice

    page.goto("http://localhost:8000/timeout-3s.html")
    time.sleep(4)
    button_locator = page.locator('button').filter(has_text='Button')
    assert button_locator.is_visible() == True, "Expected button to be visible"

@pytest.mark.parametrize('execution_number', range(7))
def test_assert_is_visible_wait_sleep_random(page: Page, execution_number):

    # Intermittently fails → Wait using time.sleep is not a good practice as delays may vary

    page.goto("http://localhost:8000/timeout-random.html")
    time.sleep(4)
    button_locator = page.locator('button').filter(has_text='Button')
    button_is_visible = button_locator.is_visible()
    assert button_is_visible == True, "Expected button to be visible"


def test_assert_is_visible_poling(page: Page):

    # Passes → is_visible with polling will wait

    page.goto("http://localhost:8000/timeout-random.html")
    button_locator = page.locator('button').filter(has_text='Button')


    polling.poll(
        lambda: button_locator.is_visible(),
        check_success=lambda x: x == True,  # Optional
        step=1,
        timeout=10,
    )

    button_locator.click()


    # button_is_visible = button_locator.is_visible()
    # assert button_is_visible == True, "Expected button to be visible"


def test_expect_to_be_visible(page: Page):

    # Passes → expect.to_be_visible() will wait
    # See: https://playwright.dev/python/docs/api/class-locatorassertions#locator-assertions-to-be-visible

    page.goto("http://localhost:8000/timeout-3s.html")
    button_locator = page.locator('button').filter(has_text='Button')
    expect(button_locator).to_be_visible()


def test_expect_to_be_visible_timeout(page: Page):

    # Passes -> larger timeout for to_be_visible()

    page.goto("http://localhost:8000/timeout-7s.html")
    button_locator = page.locator('button').filter(has_text='Button')
    expect(button_locator).to_be_visible(timeout=15000)


def test_expect_to_be_visible_timeout_polling(page: Page):

    # Passes → Expect to be visible with polling

    page.goto("http://localhost:8000/timeout-7s.html")
    button_locator = page.locator('button').filter(has_text='Button')
    polling.poll(
        lambda: expect(button_locator).to_be_visible(),
        step=1,
        timeout=35,
        check_success=lambda _: button_locator.is_visible(),
        ignore_exceptions=(AssertionError,)
    )
    button_locator.click()


@pytest.mark.parametrize('execution_number', range(7))
def test_expect_to_be_visible_intermittent(page: Page, execution_number):

    # Intermittently fails → hidden logic or intermittent behaviour

    page.goto("http://localhost:8000/timeout-3s-intermittent.html")
    button_locator = page.locator('button').filter(has_text='Button')
    expect(button_locator).to_be_visible(timeout=5000)


def test_expect_to_be_visible_timeout_reload(page: Page):

    # Passes → Handles intermittent behaviour with reloads

    page.goto("http://localhost:8000/timeout-3s-intermittent.html")
    button_locator = page.locator('button').filter(has_text='Button')

    def check():
        log.debug("Reloading page")
        page.reload()
        expect(button_locator).to_be_visible()
        return True # or use check_success

    polling.poll(
        lambda: check(),
        step=1,
        timeout=30,
        ignore_exceptions=(AssertionError,)
    )
    button_locator.click()

def test_assert_is_visible_timeout_reload(page: Page):

    # Passes → Handles intermittent behaviour with reloads

    page.goto("http://localhost:8000/intermittent.html")
    button_locator = page.locator('button').filter(has_text='Button')

    def check():
        page.reload()
        return button_locator.is_visible()

    polling.poll(
        lambda: check(),
        step=1,
        timeout=30,
    )
    button_locator.click()
