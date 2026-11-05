import pytest
from pages.otp_login_section import OTPLogin

import time

@pytest.mark.otp_login_section
def test_submit_username_without_otp(driver):
    c = OTPLogin(driver)
    c.load()
    
    c.insert_username("name random")
    c.press_submit_button()

    assert c.get_login_message() == "Please enter all 6 OTP digits."

@pytest.mark.otp_login_section
def test_submit_valid_otp(driver):
    c = OTPLogin(driver)
    c.load()

    c.insert_username("some random name")
    c.press_fetch_otp_button()
    otp_code = c.get_otp_from_new_tab()
    c.insert_otp_code(otp_code)
    c.press_submit_button()

    assert "Login successful!" in c.get_login_message()

@pytest.mark.otp_login_section
def test_test_submit_invalid_otp(driver):
    c = OTPLogin(driver)
    c.load()

    c.insert_username("some random name")
    c.press_fetch_otp_button()
    otp_code = c.get_otp_from_new_tab()
    otp_code = "123456" if otp_code != "123456" else "654321" #make sure that inserting a wrong OTP code on purpose
    
    c.insert_otp_code(otp_code)
    c.press_submit_button()

    assert "Invalid OTP. Check the code" in c.get_login_message()


@pytest.mark.otp_login_section
def test_submit_when_otp_expires(driver):
    c = OTPLogin(driver)
    c.load()

    c.insert_username("some random name")
    c.press_fetch_otp_button()
    otp_code = c.get_otp_from_new_tab()

    c.wait_for_otp_exparation()
    c.insert_otp_code(otp_code)
    c.press_submit_button()

    assert "OTP has expired." in c.get_login_message()

@pytest.mark.otp_login_section
def test_resend_otp_and_submit(driver):
    c = OTPLogin(driver)
    c.load()
    
    c.insert_username("JohnJohnson")
    c.press_fetch_otp_button()

    c.wait_for_otp_exparation()
    c.press_resend_otp_button()
    otp_code = c.get_otp_from_new_tab()
    c.insert_otp_code(otp_code)
    c.press_submit_button()

    assert "Login successful!" in c.get_login_message()
