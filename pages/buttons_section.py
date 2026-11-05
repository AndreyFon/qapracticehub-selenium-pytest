from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class ButtonsSection(BasePage):
    ANCHOR = "buttons"
    DATATEST_ID_CLASS = "nav-buttons"

    def __init__(self, driver):
        super().__init__(driver)


    def load(self):
        self.open(self.ANCHOR, self.DATATEST_ID_CLASS)


    # locators
    BUTTON_ACTION_OUTPUT = (By.ID, "button-output")

    PRIMARY_BUTTON = (By.ID, "btn-primary")
    SECONDARY_BUTTON = (By.ID, "btn-secondary")
    LEFT_CLICK_BUTTON = (By.ID, "btn-left-click")
    OUTLINE_BUTTON = (By.ID, "btn-outline")
    DISABLED_BUTTON = (By.ID, "btn-disabled")
    CLICK_COUNTER_BUTTON = (By.ID, "btn-click-counter")
    DOUBLE_CLICK_BUTTON = (By.ID, "btn-double-click")
    RIGHT_CLICK_BUTTON = (By.ID, "btn-right-click")
    HOVER_BUTTON = (By.ID, "btn-hover")
    DANGER_BUTTON = (By.ID, "btn-danger")
    NEXT_PAGE_BUTTON = (By.ID, "btn-next-page")
    DOWNLOAD_BUTTON = (By.ID, "btn-download")
    POPUP_BUTTON = (By.ID, "btn-open-popup")
    INFO_BUTTON = (By.ID, "info-btn-click")
    INFO_HOVER_BUTTON = (By.ID, "info-btn-hover")

    # methods

    def get_button_action_output(self):
        return self.find_visible(self.BUTTON_ACTION_OUTPUT).text

    def primary_button(self):
        return self._generic_click(self.PRIMARY_BUTTON)
    
    def secondary_button(self):
        return self._generic_click(self.SECONDARY_BUTTON)

    def left_click_button(self):
        return self._generic_click(self.LEFT_CLICK_BUTTON)

    def outline_button(self):
        return self._generic_click(self.OUTLINE_BUTTON)

    def disabled_button(self):
        #the expected behaviour is that you cant click the button
        return self.find_clickable(self.DISABLED_BUTTON)

    def click_counter_button(self):
        return self._generic_click(self.CLICK_COUNTER_BUTTON)

    def double_click_button(self):
        element = self.find_clickable(self.DOUBLE_CLICK_BUTTON)
        self.actions.double_click(element).perform()
        return self

    def right_click_button(self):
        element = self.find_clickable(self.RIGHT_CLICK_BUTTON)
        self.actions.context_click(element).perform()
        return self

    def hover_button(self):
        element = self.find_clickable(self.HOVER_BUTTON)
        self.actions.move_to_element(element).perform()
        return self

    def danger_button(self):
        return self._generic_click(self.DANGER_BUTTON)

    def next_page_button(self):
        return self._generic_click(self.NEXT_PAGE_BUTTON)

    #interact with content from the next_page_button
    def verify_landed_on_next_page(self):
        element = self.find_visible((By.ID, "next-page-title"))
        return element.text

    def download_button(self):
        return self._generic_click(self.DOWNLOAD_BUTTON)

    def popup_button(self):
        return self._generic_click(self.POPUP_BUTTON)

    #close the popup after pressing popup_button
    def close_popup(self):
        element = self.find_clickable((By.ID, "buttons-popup-close"))
        self.actions.move_to_element(element).click().perform()
        return self

    def click_info_button(self):
        return self._generic_click(self.INFO_BUTTON)

    def check_click_info_appeared(self):
        #the info is hidden by default and appear after clicking.
        try:
            element = self.find_visible((By.ID, "info-popup-click"))
        except(TimeoutException):
            return False
        else:
            return True

    def move_to_info_hover_button(self):
        element = self.find_clickable(self.INFO_HOVER_BUTTON)
        self.actions.move_to_element(element).perform()
        return self

    def check_hover_info_appeared(self):
        #the info is hidden by default and appear after hovering.
        try:
            element = self.find_visible((By.ID, "info-popup-hover"))
        except(TimeoutException):
            return False
        else:
            return True
            