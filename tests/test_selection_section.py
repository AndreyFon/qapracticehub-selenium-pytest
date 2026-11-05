import pytest
from pages.selection_section import SelectionSection


@pytest.mark.selection_section
def test_gender_radio_buttons(driver):
    c = SelectionSection(driver)
    c.load()

    gender = "other"
    c.check_gender_radio_button(gender)
    assert gender == c.get_gender_radio_output() #check that changed to the selected gender from the default

@pytest.mark.selection_section
def test_skill_checkboxes(driver):
    c = SelectionSection(driver)
    c.load()

    c.check_skills_checkboxes(["cypress", "selenium"]) 
    assert c.get_skills_checkbox_output() == "selenium, cypress"

@pytest.mark.selection_section
def test_single_select_dropdown(driver):
    c = SelectionSection(driver)
    c.load()

    country = "portugal"
    c.select_single_dropdown(country)
    #the search is using value attribute in 'Select' object which all small case but output is with capital letter
    assert c.get_single_dropdown_output() == country[0].upper()+country[1:]

@pytest.mark.selection_section
def test_multi_select_listbox(driver):
    c = SelectionSection(driver)
    c.load()

    languages = ["csharp", "python", "ruby"]
    c.select_from_listbox(languages)
    assert c.get_listbox_language_output() == "Python, C#, Ruby"

@pytest.mark.selection_section
def test_multi_select_dropdown(driver):
    c = SelectionSection(driver)
    c.load()

    frameworks = ["selenium", "cypress", "appium", "junit"]
    c.select_multi_dropdown(frameworks)
    assert c.get_multi_dropdown_output() == "Selenium, Cypress, Appium, JUnit"

@pytest.mark.selection_section
def test_experience_range_slider(driver):
    c = SelectionSection(driver)
    c.load()

    experience_years = 3
    c.select_range_slider(experience_years) #imitates user input on the slider by using arrow keys to move the slider
    assert c.get_experience_range_output() == f"{experience_years} years"

@pytest.mark.selection_section
@pytest.mark.skip(reason="Not implemented yet: color input value has to be set via JavaScript.")
def test_color_picker(driver):
    c = SelectionSection(driver)
    c.load()

    color = "#eb4b4b"
    c.pick_color(color) 
    assert c.get_color_picker_output() == color

@pytest.mark.selection_section
def test_enable_notifications_toggle(driver):
    c = SelectionSection(driver)
    c.load()

    c.notifications_toggle()
    assert c.get_notification_toggle_output() == "On"

@pytest.mark.selection_section
def test_auto_complete_input(driver):
    c = SelectionSection(driver)
    c.load()

    letters = "ind"
    country = "Indonesia"
    c.insert_auto_complete_input(letters)
    c.choose_from_auto_complete_options(country)
    assert c.get_auto_complete_output() == country