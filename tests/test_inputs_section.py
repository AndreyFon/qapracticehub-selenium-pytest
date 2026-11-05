import pytest
from pages.inputs_section import InputSection
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

import time


@pytest.mark.inputs_section
def test_insert_text_email_password(driver):
    c = InputSection(driver)
    c.load()

    c.insert_text("Alexander Makedon")
    c.insert_email("Alexander@RomeEmpire.rome")
    c.insert_password("Great_Library_Of_Alexandria")

    assert c.get_text() == "Alexander Makedon"
    assert c.get_email() == "Alexander@RomeEmpire.rome"
    assert c.get_password() == "Great_Library_Of_Alexandria"

@pytest.mark.inputs_section
@pytest.mark.xfail(strict=True, reason="BUG: Can set the number input to be bigger than 100.")
def test_numbers_setting_via_input(driver):
    c = InputSection(driver)
    c.load()

    #setting via input ignores the min and max
    c.insert_number_input(12345)

    assert int(c.get_number()) <= 100 #Maybe do different, check if '100' and do xfail because went above the max


@pytest.mark.inputs_section
def test_numbers_arrows_getting_below_min(driver):
    c = InputSection(driver)
    c.load()

    c.insert_number_input(2) 
    c.insert_number_actions(5, "down")

    #clicking 5 times but should not go below min: 1
    assert c.get_number() == "1" 

@pytest.mark.inputs_section
def test_numbers_arrows_getting_above_max(driver):
    c = InputSection(driver)
    c.load()

    c.insert_number_input(98) 
    c.insert_number_actions(5, "up")

    #clicking 5 times but should not go above max: 100
    assert c.get_number() == "100"

@pytest.mark.inputs_section
def test_insert_date_and_get_date(driver):
    c = InputSection(driver)
    c.load()

    c.insert_date()

    assert c.get_date() == "1995-02-01"

@pytest.mark.inputs_section
def test_time_tst(driver):
    c = InputSection(driver)
    c.load()

    #insert 70:70 and then check that the time shows: 07:59. Boundery check, that only accepts correct time values.
    c.insert_time(h=70, m=70)

    assert "07:59" == c.get_time()

#NOTE: NOT STAND ALONE SEARCH JUST CHECKING CAN INTERACT WITH THE ELEMENT. USE IT IN A TEST THAT CHECKS INSERTION OF MULTIPLE INPUTS AGAINST DEFAULT VALUES.
@pytest.mark.inputs_section
def test_can_insert_and_read_search_input(driver):
    c = InputSection(driver)
    c.load()

    text = "text for searching"
    c.insert_search(text)

    assert c.get_search() == text

@pytest.mark.inputs_section
def test_phone_input(driver):
    c = InputSection(driver)
    c.load()

    country = "Portugal"
    phone_number = "123456789"
    #select country code
    c.insert_phone_select_country(country)

    #enter phone numer, atleast 9 digits
    c.insert_phone_number(phone_number)

    #returns true if matches expected result for the given country and phone number
    assert c.is_valid_phone_number(country, phone_number)

@pytest.mark.inputs_section
def test_textarea_input(driver):
    c = InputSection(driver)
    c.load()

    text = "Random long text that have no meaning at all. Just longer then other inputs."
    c.insert_textarea(text)

    assert c.get_textarea() == text

@pytest.mark.inputs_section
def test_read_only_text(driver):
    c = InputSection(driver)
    c.load()

    c.insert_to_read_only_input("random words, some text.")

    assert c.get_read_only_input() == "Cannot edit this"

@pytest.mark.inputs_section
def test_disabled_field(driver):
    c = InputSection(driver)
    c.load()
    
    #should raise an error because the 'click_disabled_input' tries to find clickable input using the disabled input ID
    with( pytest.raises(TimeoutException) ):
        c.click_disabled_input()

@pytest.mark.inputs_section
def test_type_and_see_output(driver):
    c = InputSection(driver)
    c.load()

    text = "text to be written and then displayed below. Test, test 123."
    c.insert_type_and_see_input(text)
    
    assert c.get_type_and_see_result() == text
