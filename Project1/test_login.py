import pytest
import json
from playwright.sync_api import Page, expect
from login_page import LoginPage

# Auxiliary function to load users from JSON
def load_users():
    with open('users.json', 'r') as f:
        return json.load(f)
    
@pytest.mark.parametrize("username", load_users())
def test_login_multiple_users_json(page: Page, username):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(username, "secret_sauce")
    
    if username == "locked_out_user":
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text("Sorry, this user has been locked out")
    else:
        # Validation (Assertion)
        # Verifies if URL has changed to  /inventory.html
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

        # Verifies if we landed at products page after login
        header_title = page.locator(".title")
        expect(header_title).to_have_text("Products")

def test_login_invalid_user(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("wrong_user")
    page.get_by_placeholder("Password").fill("wrong_password")
    page.get_by_text("Login").click()

    # Validates if error message has appeared
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Username and password do not match any user")