from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.actions = ActionChains(driver)

    #I put the URL in the BasePage from the logic that in this project only the sections will be tested and interacted.
    MAIN_URL = "https://qapracticehub.com/"

    # general methods
    def find_visible(self, params_tuple = (By.CLASS_NAME, "btn")):
        ''' getting with wait visible elements '''
        return self.wait.until(EC.visibility_of_element_located(params_tuple))

    def find_clickable(self, params_tuple = (By.CLASS_NAME, "btn")):
        ''' getting with wait clickable elements  '''
        return self.wait.until(EC.element_to_be_clickable(params_tuple))

    def find_presence(self, params_tuple = (By.CLASS_NAME, "btn")):
        ''' getting with wait elements that are present '''
        return self.wait.until(EC.presence_of_element_located(params_tuple))

    def find_all_presence(self, params_tuple=(By.CLASS_NAME, "btn")):
        ''' getting with wait all the present elements ''' 
        return self.wait.until(EC.presence_of_all_elements_located(params_tuple))

    def find_all_visible(self, params_tuple=(By.CLASS_NAME, "btn")):
        ''' getting with wait all the visible elements '''
        return self.wait.until(EC.visibility_of_all_elements_located(params_tuple))

    
    #each section loads itself from the main webpage by clicking the section simulating user click
    def open(self, anchor, datatest_id_class):
        self.driver.get(self.MAIN_URL)
        nav_link = (By.CSS_SELECTOR, f"a[href='#{anchor}']")
        self.find_presence(nav_link).click()
        #wait as a check that the section is 'active'
        nav_link = (By.CSS_SELECTOR, f"a[data-testid='{datatest_id_class}']")
        self.find_visible(nav_link)

    # generic methods used almost evrytime. They use find by visibility
    def _generic_insert(self, text, locator):
        element = self.find_visible(locator)
        element.send_keys(text)
        return self

    def _generic_get(self, locator):
        return self.find_visible(locator).get_attribute("value")

    def _get_attribute(self, locator, attribute_name):
        #return attribute of an element
        return self.find_visible(locator).get_attribute(attribute_name)

    def _generic_click(self, locator):
        #moves to locator and performs click with actions
        element = self.find_visible(locator)
        self.actions.move_to_element(element).click().perform()
        return self

    def get_custom_wait_object(self, timeout=31):
        #return a WebDriverWait() object with different timeout than the default one. For when a different timeout than 10 seconds needed.
        return WebDriverWait(self.driver, timeout)