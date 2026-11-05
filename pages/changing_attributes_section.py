from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ChangingAttributes(BasePage):
    ANCHOR = "changing-attrs"
    DATATEST_ID_CLASS = "nav-changing-attrs"    

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open(self.ANCHOR, self.DATATEST_ID_CLASS)

    #locators
    clock_attribute_output = (By.ID, "attrs-clock-readout")
    rotating_status_output = (By.ID, "attrs-status-output")
    flip_id_output = (By.ID, "flip-id-readout")
    countdown_output = (By.ID, "attrs-countdown-output")
    mutating_link_output = (By.ID, "attrs-link-readout")
    #NOTE: the locators for buttons, inputs and interactable elements that are tested not included here as class variables because the whole exercise is attributes that change.

    #methods
    def click_clock_button_with_timestamp(self, timestamp):
        self._generic_click((By.CSS_SELECTOR, f"button[data-epoch='{timestamp}']"))
        return self 

    def get_clock_attributes_readout(self):
        return self.find_visible(self.clock_attribute_output).text

    def click_when_button_status_ready(self):
        element = self.find_visible((By.CSS_SELECTOR, "button[data-status='ready']"))
        self.actions.move_to_element(element).click().perform()
        return self

    def get_rotating_status_output(self):
        return self.find_visible(self.rotating_status_output).text

    #NOTE: the website says to use the stable attribute instead of catching the changing ID. 
    #Which is just regular element lookup, the guess is that to use some other attribute than the common: ID and NAME.
    def write_into_changing_id_input(self, text):
        return self._generic_insert(text, (By.CSS_SELECTOR, "input[data-testid='flip-id-input']"))
        
    def get_text_inside_changing_id_input(self):
        return self._generic_get((By.CSS_SELECTOR, "input[data-testid='flip-id-input']"))

    def get_flip_id_readout(self):
        return self.find_visible(self.flip_id_output).text

    def click_countdown_button_when_enabled(self):
        element = self.find_clickable((By.CSS_SELECTOR, "button[data-ready='true']"))
        self.actions.move_to_element(element).click().perform()
        return self

    def get_countdown_output(self):
        return self.find_visible(self.countdown_output).text

    def click_link_with_certain_attribute_value(self, href_value, title_value):
        element = self.find_presence((By.CSS_SELECTOR, f"a[href='{href_value}'][title='{title_value}']"))
        self.actions.move_to_element(element).click().perform()
        return element.get_attribute("href")

    def _click_to_remove_cookie_message(self):
        element = self.find_clickable( (By.ID, "cookie-decline") )
        self.actions.move_to_element(element).click().perform()

    def get_mutating_link_readout(self):
        return self.find_visible(self.mutating_link_output).text