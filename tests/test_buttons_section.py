import pytest
from pages.buttons_section import ButtonsSection
from selenium.common.exceptions import TimeoutException

@pytest.mark.buttons_section
def test_primary_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.primary_button()
    assert c.get_button_action_output() == "Primary button clicked." 

@pytest.mark.buttons_section
def test_secondary_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.secondary_button()
    assert c.get_button_action_output() == "Secondary button clicked." 

@pytest.mark.buttons_section
def test_left_click_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.left_click_button()
    assert c.get_button_action_output() == "Left click detected!" 

@pytest.mark.buttons_section
def test_outline_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.outline_button()
    assert c.get_button_action_output() == "Outline button clicked." 

@pytest.mark.buttons_section
def test_disabled_button(driver):
    c = ButtonsSection(driver)
    c.load()

    #expecting to fail because trying to find a clickable button
    with(pytest.raises(TimeoutException)):
        c.disabled_button()

@pytest.mark.buttons_section
def test_click_counter_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.click_counter_button()
    assert c.get_button_action_output() == "Button clicked 1 time(s)." 


@pytest.mark.buttons_section
def test_double_click_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.double_click_button()
    assert c.get_button_action_output() == "Double click detected!" 

@pytest.mark.buttons_section
def test_right_click_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.right_click_button()
    assert c.get_button_action_output() == "Right click detected!" 

@pytest.mark.buttons_section
def test_hover_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.hover_button()
    assert c.get_button_action_output() == "Mouse entered the hover button." 

@pytest.mark.buttons_section
def test_danger_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.danger_button()
    assert c.get_button_action_output() == "Danger button clicked." 

@pytest.mark.buttons_section
def test_next_page_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.next_page_button()
    #NOTE: for now just check that landed on the next page. 
    assert c.verify_landed_on_next_page() == "Successfully landed on the new page"

@pytest.mark.buttons_section
@pytest.mark.skip(reason="Not implemented yet: needs Chrome download preferences and a temp dir to verify the file.")
def test_download_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.download_button()
    assert c.get_button_action_output() == "Sample file download started." 

@pytest.mark.buttons_section
def test_popup_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.popup_button()
    assert c.get_button_action_output() == "Popup opened."
    c.close_popup()
    assert c.get_button_action_output() == "Popup closed." 

@pytest.mark.buttons_section
def test_info_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.click_info_button()
    assert c.check_click_info_appeared() #true when found the info after clicking and false if the element still hidden

@pytest.mark.buttons_section
def test_info_hover_button(driver):
    c = ButtonsSection(driver)
    c.load()

    c.move_to_info_hover_button()
    assert c.check_hover_info_appeared()

