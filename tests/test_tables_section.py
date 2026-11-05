import pytest
from pages.tables_section import TablesSection
import time

@pytest.mark.tables_section
def test_sort_by_name(driver):
    c = TablesSection(driver)
    c.load()

    own_sorted_data = c.own_sort_table_data(is_reverse=True) #reverse because by default the data sorted already by 'name' when website opened

    c.click_sort_name_button()
    c.click_sort_name_button()
    sorted_by_button_data = c.get_current_table_data()

    assert sorted_by_button_data == own_sorted_data

@pytest.mark.tables_section
def test_sort_by_age(driver):
    c = TablesSection(driver)
    c.load()

    own_sorted_data = c.own_sort_table_data(column="age")

    c.click_sort_age_button()
    sorted_by_button_data = c.get_current_table_data()

    assert sorted_by_button_data == own_sorted_data

@pytest.mark.tables_section
def test_filter_by_name(driver):
    c = TablesSection(driver)
    c.load()

    c.insert_text_into_filter_by_name_input("bob")
    assert len(c.get_current_table_data()) == 1 #should be only 1 matching row after filter by name


@pytest.mark.tables_section
def test_add_one_new_user(driver):
    c = TablesSection(driver)
    c.load()

    new_user_data = {"id": 20, "name": "Stuart", "email": "little@mail.net", "role": "Tester", "age": 41}

    c.click_add_new_user_button() 
    c.fill_new_user_data(new_user_data)
    c.click_save_users_button()
    
    assert c.check_table_has_user(new_user_data)

@pytest.mark.tables_section
def test_add_multiple_new_users(driver):
    c = TablesSection(driver)
    c.load()

    new_user_data_1 = {"id": 20, "name": "Stuart", "email": "little@mail.net", "role": "Tester", "age": 41}
    new_user_data_2 = {"id": 21, "name": "Greg", "email": "Grog@mail.net", "role": "Admin", "age": 100}

    c.click_add_new_user_button() 
    c.fill_new_user_data(new_user_data_1)
    c.click_add_another_user_button_in_popup()
    c.fill_new_user_data(new_user_data_2)

    c.click_save_users_button()

    assert len(c.get_current_table_data()) == 10 #10 because the table by default has 8 users and we tried to add 2 more

@pytest.mark.tables_section
def test_adding_new_user_with_existing_id(driver):
    c = TablesSection(driver)
    c.load()

    new_user_data = {"id": 1, "name": "Stuart", "email": "little@mail.net", "role": "Tester", "age": 41}

    c.click_add_new_user_button() 
    c.fill_new_user_data(new_user_data)
    c.click_save_users_button()
    
    assert c.is_error_message_shown_in_new_user_popup()

@pytest.mark.tables_section
def test_checkboxes_row_selection(driver):
    c = TablesSection(driver)
    c.load()

    c.click_checkbox() #without parameter by default is '1'
    c.click_checkbox(3)

    assert c.get_table_selection_output() == "2 row(s) selected"

@pytest.mark.tables_section
def test_select_all_checkboxes(driver):
    c = TablesSection(driver)
    c.load()
    
    c.click_select_all_checkboxes()
    assert c.get_table_selection_output() == "4 row(s) selected"
