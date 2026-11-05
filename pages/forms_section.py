from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class FormsSection(BasePage):
    
    ANCHOR = "forms"
    DATATEST_ID_CLASS = "nav-forms"
    
    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open(self.ANCHOR, self.DATATEST_ID_CLASS)

    # LOCATORS
    LOGIN_BUTTON = (By.ID, "login-submit")
    FORGOT_PASSWORD_BUTTON = (By.ID, "forgot-password-trigger")
    REGISTER_BUTTON = (By.ID, "register-submit")
    CLEAR_BUTTON = (By.ID, "register-clear")
    LOGIN_PASSWORD_VISIBILITY_BUTTON = (By.ID, "login-password-toggle")

    FORGOT_PASSWORD_SUBMIT_BUTTON = (By.ID, "forgot-password-submit")

    CORRECT_USERNAME = (By.ID, "login-preview-username") # given right username for the Login form
    CORRECT_PASSWORD = (By.ID, "login-preview-password") # given right password for the Login form

    FORGOT_PASSWORD_USERNAME_INPUT = (By.ID, "forgot-username")

    USERNAME_INPUT = (By.ID, "login-username")
    PASSWORD_INPUT = (By.ID, "login-password")
    FIRST_NAME_REGISTRATION = (By.ID, "reg-firstname")
    LAST_NAME_REGISTRATION = (By.ID, "reg-lastname")
    EMAIL_REGISTRATION = (By.ID, "reg-email")
    COUNTRY_SELECTION = (By.ID, "reg-country")  # currently using the 'select'(id:reg-country) element, another option to use 'options' element of each country

    LOGIN_STATUS_MESSAGE = (By.ID, "login-message")
    FORGOT_PASSWORD_MESSAGE = (By.ID, "forgot-password-result") 
    REGISTRATION_MESSAGE = (By.ID, "register-message")

    # GENERIC METHODS
    def _generic_insert(self, text, locator):
        element = self.find_visible(locator)
        self.actions.move_to_element(element).click().perform()
        self.actions.send_keys(text).perform()
        return self

    def _generic_button_click(self, locator):
        element = self.find_clickable(locator)
        self.actions.move_to_element(element).click().perform()
        return self

    def _click_to_remove_cookie_message(self):
        element = self.find_clickable( (By.ID, "cookie-decline") )
        self.actions.move_to_element(element).click().perform()

    # METHODS
    def insert_username(self, text):
        return self._generic_insert(text, self.USERNAME_INPUT)

    def insert_password(self, text):
        return self._generic_insert(text, self.PASSWORD_INPUT)

    def get_correct_username(self):
        return self.find_presence(self.CORRECT_USERNAME).text

    def get_correct_password(self):
        return self.find_presence(self.CORRECT_PASSWORD).text

    def press_form_password_visibility_button(self):
        self._generic_button_click(self.LOGIN_PASSWORD_VISIBILITY_BUTTON)
        return self

    def is_password_visible_in_login(self):
        element = self.find_clickable(self.LOGIN_PASSWORD_VISIBILITY_BUTTON)
        if("true" == element.get_attribute("aria-pressed")):
            return True
        else:
            return False

    def insert_forgot_password_username(self, text):
        return self._generic_insert(text, self.FORGOT_PASSWORD_USERNAME_INPUT)

    def insert_first_name_registration(self, text):
        return self._generic_insert(text, self.FIRST_NAME_REGISTRATION)

    def insert_last_name_registration(self, text):
        return self._generic_insert(text, self.LAST_NAME_REGISTRATION)

    def insert_email_registration(self, text):
        return self._generic_insert(text, self.EMAIL_REGISTRATION)

    def choose_country(self, country):
        element = self.find_visible(self.COUNTRY_SELECTION)
        select = Select(element)
        select.select_by_visible_text(country)

    def press_register_button(self):
        return self._generic_button_click(self.REGISTER_BUTTON)

    def press_clear_button(self):
        return self._generic_button_click(self.CLEAR_BUTTON)

    def press_login_button(self):
        return self._generic_button_click(self.LOGIN_BUTTON)

    def press_forgot_password_button(self):
        return self._generic_button_click(self.FORGOT_PASSWORD_BUTTON)

    def press_submit_button_in_forgot_password(self):
        return self._generic_button_click(self.FORGOT_PASSWORD_SUBMIT_BUTTON)

    def is_password_displayed_in_forgot_password(self):
        # the self.FORGOT_PASSWORD_MESSAGE only visible when the correct user name submitted otherwise its hidden
        element = self.find_presence(self.FORGOT_PASSWORD_MESSAGE)
        if(element.is_displayed()):
            return True
        else:
            return False

    def is_login_successful(self):
        element = self.find_visible(self.LOGIN_STATUS_MESSAGE)
        if("Login successful! Welcome," in element.text):
            return True
        else:
            return False

    def is_registration_successful(self):
        element = self.find_visible(self.REGISTRATION_MESSAGE)
        if("success" in element.get_attribute("class")):
            return True
        else:
            return False

    def is_registration_inputs_empty(self):
        if(self._get_attribute(self.FIRST_NAME_REGISTRATION, "value") != ""):
            return False
        
        if(self._get_attribute(self.LAST_NAME_REGISTRATION, "value") != ""):
            return False
        
        if(self._get_attribute(self.EMAIL_REGISTRATION, "value") != ""):
            return False
        
        element = self.find_visible(self.COUNTRY_SELECTION)
        select = Select(element)
        if(select.first_selected_option.text != "Select country"):
            return False
        return True
        