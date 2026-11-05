from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class SelectionSection(BasePage):
    
    ANCHOR = "selection"
    DATATEST_ID_CLASS = "nav-selection"

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open(self.ANCHOR, self.DATATEST_ID_CLASS)

    # locators
    GENDER_RADIO_BUTTONS = (By.ID, "gender-fieldset")
    SKILLS_CHECKBOXES = (By.ID, "skills-fieldset")
    SINGLE_SELECT_DROPDOWN = (By.ID, "country-select")
    MULTI_SELECT_LISTBOX = (By.ID, "languages-select")
    MULTI_SELECT_DROPDOWN_BUTTON = (By.ID, "frameworks-multi-select-trigger")

    EXPERIENCE_RANGE_SLIDER = (By.ID, "experience-range")
    COLOR_PICKER = (By.ID, "color-input")
    ENABLE_NOTIFICATIONS_TOGGLE = (By.ID, "toggle-notifications")
    AUTO_COMPLETE_INPUT = (By.ID, "autocomplete-input")

    GENDER_RADIO_BUTTONS_OUTPUT = (By.ID, "gender-output")
    SKILLS_CHECKBOXES_OUTPUT = (By.ID, "skills-output")
    COUNTRY_DROPDOWN_OUTPUT = (By.ID, "country-output")
    MULTI_SELECT_LISTBOX_OUTPUT  = (By.ID, "languages-output")
    MULTI_SELECT_DROPDOWN_OUTPUT    = (By.ID, "frameworks-multi-output")
    EXPERIENCE_RANGE_OUTPUT = (By.ID, "experience-output")
    COLOR_PICKER_OUTPUT = (By.ID, "color-output")
    NOTIFICATIONS_TOGGLE_OUTPUT = (By.ID, "toggle-output")
    AUTO_COMPLETE_OUTPUT = (By.ID, "autocomplete-output")

    # methods

    def check_gender_radio_button(self, option):
        # the gender radio button have id in the format 'gender-option' where option is: male, female, other.
        return self._generic_click((By.ID, f"gender-{option}"))

    def get_gender_radio_output(self):
        return self._generic_get(self.GENDER_RADIO_BUTTONS_OUTPUT)

    def check_skills_checkboxes(self, options=None):
        # the skills checkboxes have idea of the form 'skill-selenium'
        if(isinstance(options, list)):
            for o in options: 
                self._generic_click( (By.ID, f"skill-{o}") )
        else:
            self._generic_click( (By.ID, f"skill-{options}") )
        return self

    def get_skills_checkbox_output(self):
        return self._generic_get(self.SKILLS_CHECKBOXES_OUTPUT)

    def select_single_dropdown(self, country):
        element = self.find_clickable(self.SINGLE_SELECT_DROPDOWN)
        select = Select(element)
        select.select_by_value(country)
        return self

    def get_single_dropdown_output(self):
        return self._generic_get(self.COUNTRY_DROPDOWN_OUTPUT)

    def select_from_listbox(self, options=[]):
        element = self.find_clickable(self.MULTI_SELECT_LISTBOX)
        select = Select(element)
        if(type(options) == type([])):
            for o in options:
                select.select_by_value(o)
        else:
            select.select_by_value(options)
        return self

    def get_listbox_language_output(self):
        return self._generic_get(self.MULTI_SELECT_LISTBOX_OUTPUT)

    def select_multi_dropdown(self, options=None):
        element = self.find_clickable(self.MULTI_SELECT_DROPDOWN_BUTTON)
        self.actions.move_to_element(element).click().perform()

        if(options is not None):
            for o in options:
                element = self.find_clickable((By.ID, f"framework-{o}"))
                self.actions.move_to_element(element).click().perform()
        return self

    def get_multi_dropdown_output(self):
        return self._generic_get(self.MULTI_SELECT_DROPDOWN_OUTPUT)

    def select_range_slider(self, value):
        element = self.find_visible(self.EXPERIENCE_RANGE_SLIDER)
        self.actions.move_to_element(element).click().perform()
        
        current_value = int(self._generic_get(self.EXPERIENCE_RANGE_OUTPUT).split(" ")[0])
        key_to_press = Keys.ARROW_RIGHT if (value-current_value) > 0 else Keys.ARROW_LEFT
        
        for _ in range(abs(value-current_value)):
            self.actions.send_keys(key_to_press).perform()
        return self

    def get_experience_range_output(self):
        return self._generic_get(self.EXPERIENCE_RANGE_OUTPUT)


    def pick_color(self, color):
        self._generic_insert(color, self.COLOR_PICKER)
        return self

    def get_color_picker_output(self):
        return self._generic_get(self.COLOR_PICKER_OUTPUT)

    def notifications_toggle(self):
        # no parameter because should just flip the current value
        element = self.find_presence(self.ENABLE_NOTIFICATIONS_TOGGLE)
        self.actions.move_to_element(element).click().perform()
        return self

    def get_notification_toggle_output(self):
        return self._generic_get(self.NOTIFICATIONS_TOGGLE_OUTPUT)

    def insert_auto_complete_input(self, text):
        return self._generic_insert(text, self.AUTO_COMPLETE_INPUT)

    def choose_from_auto_complete_options(self, option):
        #after inserting at least 3 letter options displayed to choose from, this selects one of them
        elements = self.find_all_presence((By.CSS_SELECTOR, "ul[id='autocomplete-suggestions'] > li[role='option']"))
        for e in  elements:
            if( e.get_attribute("data-country") == option ):
                self.actions.move_to_element(e).click().perform()
        return self

    def get_auto_complete_output(self):
        return self._generic_get(self.AUTO_COMPLETE_OUTPUT)