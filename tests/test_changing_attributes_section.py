import pytest
from pages.changing_attributes_section import ChangingAttributes
import time

@pytest.mark.changing_attributes
def test_clock_attributes_button(driver):
    c = ChangingAttributes(driver)
    c.load()

    timestamp_in_5_seconds = int(time.time()) + 5
    
    c.click_clock_button_with_timestamp(timestamp_in_5_seconds)
    
    assert str(timestamp_in_5_seconds) in c.get_clock_attributes_readout()
    

@pytest.mark.changing_attributes
def test_rotating_status_button(driver):
    c = ChangingAttributes(driver)
    c.load()

    c.click_when_button_status_ready()

    assert int(c.get_rotating_status_output()[-1]) == 1

@pytest.mark.changing_attributes
def test_changing_id(driver):
    c = ChangingAttributes(driver)
    c.load()

    test_text = "Random words for testing. 123456789"
    c.write_into_changing_id_input(test_text)

    assert c.get_text_inside_changing_id_input() == test_text

@pytest.mark.changing_attributes
def test_countdown_button(driver):
    c = ChangingAttributes(driver)
    c.load()

    c.click_countdown_button_when_enabled()

    assert c.get_countdown_output() == "Submit clicked while data-ready=true"

@pytest.mark.changing_attributes
def test_mutating_link(driver):
    c = ChangingAttributes(driver)
    c.load()

    t = 3

    element_href = c.click_link_with_certain_attribute_value(f"https://qapracticehub.com/demo-ticket?t={t}", f"Ticket t={t}")
    assert c.get_mutating_link_readout() == f"Clicked link · href was {element_href}"
    
    t += 6
    element_href = c.click_link_with_certain_attribute_value(f"https://qapracticehub.com/demo-ticket?t={t}", f"Ticket t={t}")
    assert c.get_mutating_link_readout() == f"Clicked link · href was {element_href}"