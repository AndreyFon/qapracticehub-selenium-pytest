import pytest
from pages.forms_section import FormsSection
import time


@pytest.mark.forms_section
def test_login_form_input_invalid_info(driver):
    c = FormsSection(driver)
    c.load()

    c.insert_username("Random Text")
    c.insert_password("MyPasswordVeryLong")
    c.press_login_button()

    assert c.is_login_successful() == False

@pytest.mark.forms_section
def test_login_form_input_valid_info(driver):
    c = FormsSection(driver)
    c.load()

    c.insert_username(c.get_correct_username())
    c.insert_password(c.get_correct_password())
    c.press_login_button()

    assert c.is_login_successful()

@pytest.mark.forms_section
def test_check_password_visibility_in_login(driver):
    #doing this test because the hide password button is implemented on the website and not some browser default
    c = FormsSection(driver)
    c.load()

    c.insert_password(c.get_correct_password())
    c.press_form_password_visibility_button()

    assert c.is_password_visible_in_login()

@pytest.mark.forms_section
def test_forgot_password_valid_username(driver):
    c = FormsSection(driver)
    c.load()

    c.press_forgot_password_button()
    c.insert_forgot_password_username(c.get_correct_username())
    c.press_submit_button_in_forgot_password()
    
    assert c.is_password_displayed_in_forgot_password()

@pytest.mark.forms_section
def test_forgot_password_invalid_username(driver):
    c = FormsSection(driver)
    c.load()

    c.press_forgot_password_button()
    c.insert_forgot_password_username("Random Invalid Username")
    c.press_submit_button_in_forgot_password()
    
    assert c.is_password_displayed_in_forgot_password() == False

@pytest.mark.forms_section
def test_fill_valid_registration_form(driver):
    c = FormsSection(driver)
    c.load()

    c._click_to_remove_cookie_message()

    c.insert_first_name_registration("John")
    c.insert_last_name_registration("Johnson")
    c.insert_email_registration("John1991@fmail.com")
    c.choose_country("Brazil")
    c.press_register_button()
    
    assert c.is_registration_successful()

@pytest.mark.forms_section
def test_fill_invalid_registration_form(driver):
    #difference from valid test is that here last name and email are not inserted
    c = FormsSection(driver)
    c.load()

    c._click_to_remove_cookie_message()

    c.insert_first_name_registration("John")
    c.choose_country("Brazil")
    c.press_register_button()
    
    assert c.is_registration_successful() == False

@pytest.mark.forms_section
def test_registration_clear_button(driver):
    c = FormsSection(driver)
    c.load()

    c._click_to_remove_cookie_message()

    c.insert_first_name_registration("John")
    c.insert_last_name_registration("Johnson")
    c.insert_email_registration("John1991@fmail.com")
    c.choose_country("Portugal")
    c.press_clear_button()

    assert c.is_registration_inputs_empty()