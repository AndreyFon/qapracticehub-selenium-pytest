from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TablesSection(BasePage):
    ANCHOR = "tables"
    DATATEST_ID_CLASS = "nav-tables"

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open(self.ANCHOR, self.DATATEST_ID_CLASS)

    #locators
    FILTER_NAME_INPUT = (By.ID, "table-search")
    SORT_NAME_BUTTON = (By.ID, "table-sort-name")
    SORT_AGE_BUTTON = (By.ID, "table-sort-age")
    
    ADD_USER_BUTTON = (By.ID, "table-add-role")
    NEW_USER_POPUP_ID = (By.ID, "add-role-modal")
    NEW_USER_ID_INPUT = (By.CLASS_NAME, "role-id")
    NEW_USER_NAME_INPUT = (By.CLASS_NAME, "role-name")
    NEW_USER_EMAIL_INPUT = (By.CLASS_NAME, "role-email")
    NEW_USER_ROLE_SELECT = (By.CLASS_NAME, "role-role")
    NEW_USER_AGE_INPUT = (By.CLASS_NAME, "role-age")
    ADD_ANOTHER_NEW_USER_BUTTON = (By.ID, "add-role-entry-btn")
    NEW_USERS_CANCEL_BUTTON = (By.ID, "add-role-cancel")
    NEW_USERS_SAVE_BUTTON = (By.ID, "add-role-save")
    ADD_NEW_USER_ERROR_MESSAGE = (By.ID, "add-role-message")
    
    PREV_PAGE_BUTTON = (By.ID, "page-prev")
    NEXT_PAGE_BUTTON = (By.ID, "page-next")
    PAGE_INFO_TEXT_ID = (By.ID, "page-info")

    TABLE_SELECTION_OUTPUT_TEXT = (By.ID, "table-selection-output")

    SELECT_ALL_CHECKBOXES = (By.ID, "select-all-rows")

    #methods
    def click_sort_name_button(self):
        return self._generic_click(self.SORT_NAME_BUTTON)

    def click_sort_age_button(self):
        return self._generic_click(self.SORT_AGE_BUTTON)

    def insert_text_into_filter_by_name_input(self, text):
        return self._generic_insert(text, self.FILTER_NAME_INPUT)

    def click_add_new_user_button(self):
        return self._generic_click(self.ADD_USER_BUTTON)

    def click_add_another_user_button_in_popup(self):
        return self._generic_click(self.ADD_ANOTHER_NEW_USER_BUTTON)

    def get_add_new_user_error_message(self):
        return self._generic_get(self.ADD_NEW_USER_ERROR_MESSAGE)

    def get_current_table_data(self):
        ret = []
        button_click_counter = 0
            
        while True:
	        for table_row in self.find_all_visible((By.CSS_SELECTOR, "tr[data-user-id]")):
		        id_, *mid, age =  table_row.find_elements(By.CSS_SELECTOR, "td")[1:-1]
		        ret.append((int(id_.text), *[e.text for e in mid], int(age.text)))
	
	        next_page_button = self.find_presence(self.NEXT_PAGE_BUTTON)
	        if(not next_page_button.is_enabled()):
		        break
	
	        self._generic_click(self.NEXT_PAGE_BUTTON)
	        button_click_counter += 1 

        #reverse the clicks and get back to first page after finished going through all pages and getting the data from the table
        for _ in range(button_click_counter):
            self.click_prev_page_button()
        return ret

    def own_sort_table_data(self, column="name",  is_reverse=False):
        table_data = self.get_current_table_data() #List of Tuples, where each Tuble is a row from table
        
        #either default 'name' or age. Because that is what sort buttons available in the website
        if(column=="name"):
            index = 1
        else:
            index = -1

        if(is_reverse):
            return sorted(table_data, key=lambda x: x[index], reverse=True)
        else:
            return sorted(table_data, key=lambda x: x[index])

    #given dictionary with user data inputs it into the fields in the 'Add new user' popup. Expected that the popup is open/not hidden.
    def fill_new_user_data(self, data={"id": 100, "name": "Ivan", "email": "Iv@mail.net", "role": "Admin", "age": 55}):
        element = self.find_all_visible((By.CLASS_NAME, "role-entry"))

        if(len(element) > 1):
            element = element[-1]

            el = element.find_element(self.NEW_USER_ID_INPUT[0], self.NEW_USER_ID_INPUT[1])
            el.send_keys(data["id"])
            
            el = element.find_element(self.NEW_USER_NAME_INPUT[0], self.NEW_USER_NAME_INPUT[1])
            el.send_keys(data["name"])
            
            el = element.find_element(self.NEW_USER_EMAIL_INPUT[0], self.NEW_USER_EMAIL_INPUT[1])
            el.send_keys(data["email"])
            
            el = element.find_element(self.NEW_USER_AGE_INPUT[0], self.NEW_USER_AGE_INPUT[1])
            el.send_keys(data["age"])
            
            element = element.find_element(self.NEW_USER_ROLE_SELECT[0], self.NEW_USER_ROLE_SELECT[1])
            select = Select(element)
            select.select_by_value(data["role"])
        else:
            self._generic_insert(data["id"], self.NEW_USER_ID_INPUT)
            self._generic_insert(data["name"], self.NEW_USER_NAME_INPUT)
            self._generic_insert(data["email"], self.NEW_USER_EMAIL_INPUT)
            self._generic_insert(data["age"], self.NEW_USER_AGE_INPUT)
            
            element = self.find_visible(self.NEW_USER_ROLE_SELECT)
            select = Select(element)
            select.select_by_value(data["role"])
        return self

    def click_save_users_button(self):
        return self._generic_click(self.NEW_USERS_SAVE_BUTTON)

    def check_table_has_user(self, user_data={}):
        current_data_in_table = self.get_current_table_data()
        return tuple(user_data.values()) in current_data_in_table

    def is_error_message_shown_in_new_user_popup(self):
        try:
            wait_obj = self.get_custom_wait_object(timeout=2)
            wait_obj.until(EC.visibility_of_element_located(self.ADD_NEW_USER_ERROR_MESSAGE))
        except(TimeoutException):
            return False #element was not visible meaning the error message did not displayed
        else: 
            return True


    def click_prev_page_button(self):
        return self._generic_click(self.PREV_PAGE_BUTTON)

    def click_next_page_button(self):
        return self._generic_click(self.NEXT_PAGE_BUTTON)


    def click_checkbox(self, checkbox_user_id=1):
        element = self.find_clickable((By.CSS_SELECTOR, f"input[data-user-id='{checkbox_user_id}']"))
        self.actions.move_to_element(element).click().perform()
        return self

    def click_select_all_checkboxes(self):
        return self._generic_click(self.SELECT_ALL_CHECKBOXES)

    def get_table_selection_output(self):
        return self.find_visible(self.TABLE_SELECTION_OUTPUT_TEXT).text
