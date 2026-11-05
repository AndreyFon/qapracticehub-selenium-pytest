from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class OTPLogin(BasePage):
    ANCHOR = "otp-login"
    DATATEST_ID_CLASS = "nav-otp-login"
    
    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open(self.ANCHOR, self.DATATEST_ID_CLASS)


    # locators
    USERNAME_INPUT_FIELD = (By.ID, "otp-username")
    FIRST_OTP_DIGIT = (By.ID, "otp-digit-1")

    SUBMIT_BUTTON = (By.ID, "otp-submit")
    FETCH_BUTTON = (By.ID, "btn-fetch-otp")
    RESEND_OTP_BUTTON = (By.ID, "btn-resend-otp")

    OPT_COUNTDOWN_MESSAGE = (By.ID, "otp-countdown")
    OTP_LOGIN_MESSAGE = (By.ID, "otp-login-message")

    OTP_DIGITS_IN_NEW_OTP_TAB = (By.ID, "otp-display")

    # methods
    def insert_username(self, text):
        return self._generic_insert(text, self.USERNAME_INPUT_FIELD)

    def press_submit_button(self):
        return self._generic_click(self.SUBMIT_BUTTON)

    def press_fetch_otp_button(self):
        return self._generic_click(self.FETCH_BUTTON)

    def press_resend_otp_button(self):
        return self._generic_click(self.RESEND_OTP_BUTTON)

    def get_login_message(self):
        return self.find_visible(self.OTP_LOGIN_MESSAGE).text

    def get_countdown_message(self):
        return self.find_visible(self.OPT_COUNTDOWN_MESSAGE).text

    def get_otp_from_new_tab(self):
        original_window = self.driver.current_window_handle

        # go to the new opened tab with the OTP code
        for handle in self.driver.window_handles:
            if(handle != original_window):
                self.driver.switch_to.window(handle)
                break

        # get the otp number
        otp_code = self.find_visible(self.OTP_DIGITS_IN_NEW_OTP_TAB).text

        self.driver.close() # close the new tab
        self.driver.switch_to.window(original_window)  # go back
        return otp_code

    def insert_otp_code(self, text):
        return self._generic_insert(text, self.FIRST_OTP_DIGIT)

    def wait_for_otp_exparation(self):
        wait_object = self.get_custom_wait_object()
        wait_object.until(EC.text_to_be_present_in_element(self.OPT_COUNTDOWN_MESSAGE, "OTP has expired."))
        return self