from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class InputSection(BasePage):
    
    ANCHOR = "inputs"
    DATATEST_ID_CLASS = "nav-inputs"

    def __init__(self, driver):
        super().__init__(driver)

    # locators
    TEXT_INPUT = (By.ID, "text-input")
    EMAIL_INPUT = (By.ID, "email-input")
    PASSWORD_INPUT = (By.ID, "password-input")
    NUMBER_INPUT = (By.ID, "number-input")
    DATE_INPUT = (By.ID, "date-input")
    TIME_INPUT = (By.ID, "time-input")
    SEARCH_INPUT = (By.ID, "search-input")
    PHONE_INPUT = (By.ID, "tel-input")
    PHONE_PREFIX_INPUT = (By.ID, "phone-prefix")
    TEXTAREA_INPUT = (By.ID, "textarea-input")
    READ_ONLY_INPUT = (By.ID, "readonly-input")
    DISABLED_INPUT = (By.ID, "disabled-input")
    TYPE_SEE_INPUT = (By.ID, "input-output")
    TYPE_SEE_RESULT = (By.ID, "input-output-result")

    # general methods
    def get_available_phone_codes(self):
        elements = self.find_all_presence((By.CSS_SELECTOR, "li[class='phone-country-option']"))
        code_dict = {}
        for e in elements:
            data = {"country_code": "", "phone_length": ""}
            data["country_code"] = e.get_attribute("data-dial")
            data["phone_length"] = e.get_attribute("data-length")
            code_dict[e.get_attribute("textContent").split("(")[0].strip()] = data
        return code_dict
        

    def load(self):
        self.open(self.ANCHOR, self.DATATEST_ID_CLASS)
        self.PHONE_CODE_OPTIONS = self.get_available_phone_codes()

    def _generic_insert(self, text, locator):
        # default insert via sending keys to the input element
        element = self.find_visible(locator)
        element.send_keys(text)
        return self

    def _generic_get(self, locator):
        return self.find_visible(locator).get_attribute("value")

    #locators methods
    def insert_text(self, text="John Johnson"):
        return self._generic_insert(text, self.TEXT_INPUT)


    def get_text(self):
        return self._generic_get(self.TEXT_INPUT)

    def insert_email(self, text="defaulEmail@email.com"):
        return self._generic_insert(text, self.EMAIL_INPUT)

    def get_email(self):
        return self._generic_get(self.EMAIL_INPUT)

    def insert_password(self, text="qwerty123456789"):
        return self._generic_insert(text, self.PASSWORD_INPUT)

    def get_password(self):
        return self._generic_get(self.PASSWORD_INPUT)

    def insert_date(self, text="01021995"):
        return self._generic_insert(text, self.DATE_INPUT)

    def get_date(self):
        return self._generic_get(self.DATE_INPUT) 

    def insert_number_input(self, value):
        #before setting the number with value need to remove the default value "1"
        element = self.find_visible(self.NUMBER_INPUT)
        element.clear()
        return self._generic_insert(str(value), self.NUMBER_INPUT)
        

    def insert_number_actions(self, value, arrow):
        #value - how many clickes
        #arrow - keyboard arrows up OR down. To somewhat simulate the click on the GUI small arrows near number
        element = self.find_clickable(self.NUMBER_INPUT)
        self.actions.move_to_element(element).click().perform()
        for _ in range(value):
            act = self.actions.send_keys(Keys.ARROW_UP) if arrow == "up" else self.actions.send_keys(Keys.ARROW_DOWN)
            act.perform()
        return self

    def get_number(self):
        return self._generic_get(self.NUMBER_INPUT)
    
    def get_number_min_attr(self):
        return self.find_visible(self.NUMBER_INPUT).get_attribute("min")

    def get_number_max_attr(self):
        return self.find_visible(self.NUMBER_INPUT).get_attribute("max")

    def insert_time(self, h=12, m=30):
        #h - hours. m - minutes.
        return self._generic_insert(str(h)+str(m), self.TIME_INPUT)

    def get_time(self):
        return self._generic_get(self.TIME_INPUT)

    def insert_search(self, text):
        return self._generic_insert(text, self.SEARCH_INPUT)

    def get_search(self):
        return self._generic_get(self.SEARCH_INPUT)

    def insert_phone_select_country(self, country):
        # to set the country code of the phone input
        
        element = self.find_clickable( (By.ID, "cookie-decline") )
        self.actions.move_to_element(element).click().perform()

        self.actions.move_to_element(self.find_clickable(self.PHONE_PREFIX_INPUT)).click().perform()
        element = self.find_visible( (By.ID, "phone-country-list") )
        
        self.actions.move_to_element(element).perform()
        
        element = self.find_visible( (By.CSS_SELECTOR, f"li[data-dial='{self.PHONE_CODE_OPTIONS[country]['country_code']}']") )
        self.actions.move_to_element(element).click().perform()

        return self
    
    def insert_phone_number(self, text):
        #insert the phone number, need to be 9 digits
        return self._generic_insert(text, self.PHONE_INPUT)

    def get_phone_whole(self):
        #returns country code + phone
        return self._generic_get(self.PHONE_INPUT)

    def is_valid_phone_number(self, country, phone_number):
        #using 'tel-feedback' status text checking if the phone have 9 digits
        # can also check class of the 'phone-input-combo' to see if 'is-valid'
        
        status_element = self.find_visible((By.ID, "tel-feedback"))

        if(status_element.text == f"Valid {country} number: {self.PHONE_CODE_OPTIONS[country]['country_code']} {phone_number}"):
            return True
        else:
            return False

    def insert_textarea(self, text):
        return self._generic_insert(text, self.TEXTAREA_INPUT)

    def get_textarea(self):
        return self._generic_get(self.TEXTAREA_INPUT)

    def insert_to_read_only_input(self, text):
        return self._generic_insert(text, self.READ_ONLY_INPUT)

    def get_read_only_input(self):
        return self._generic_get(self.READ_ONLY_INPUT)

    def click_disabled_input(self):
        element = self.find_clickable(self.DISABLED_INPUT)
        self.actions.move_to_element(element).click().perform()

    def insert_type_and_see_input(self, text):
        return self._generic_insert(text, self.TYPE_SEE_INPUT)

    def get_type_and_see_result(self):
        return self._generic_get(self.TYPE_SEE_RESULT)
