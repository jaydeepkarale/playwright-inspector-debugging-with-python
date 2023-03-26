from playwright.sync_api import Page, expect


def test_account_page_has_continue_link(page: Page) -> None:
    page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    expect(page.get_by_role("link", name="Continue")).to_be_visible()


def test_account_login_form_has_email_and_password_fields(page: Page) -> None:
    page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    expect(page.get_by_placeholder("E-Mail Address")).to_be_visible()
    page.pause()
    expect(page.get_by_placeholder("Password")).to_be_visible()

def test_account_login_form_forgotten_password_link(page: Page) -> None:
    page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    expect(page.get_by_role("link", name="Forgotten Password", exact=True)).to_be_visible()
    