"""Selenium 3 element finding and basic element actions."""

import pytest

from selenium3_examples.pages.example_page import ExamplePage


pytestmark = pytest.mark.selenium3


def test_can_find_element_by_id(driver):
    page = ExamplePage(driver)
    page.open_web_form()

    text_input = page.text_input()

    assert text_input.is_displayed()
    assert text_input.get_attribute("id") == "my-text-id"


def test_can_find_element_by_name(driver):
    page = ExamplePage(driver)
    page.open_web_form()

    password_input = page.password_input()

    assert password_input.is_enabled()
    assert password_input.get_attribute("name") == "my-password"


def test_can_find_element_by_css_selector(driver):
    page = ExamplePage(driver)
    page.open_web_form()

    submit_button = page.submit_button()

    assert submit_button.text == "Submit"


def test_can_find_element_by_xpath(driver):
    page = ExamplePage(driver)
    page.open_web_form()

    textarea = page.textarea()

    textarea.send_keys("Selenium 3 XPath example")
    assert textarea.get_attribute("value") == "Selenium 3 XPath example"


def test_can_find_many_elements_by_css_selector(driver):
    page = ExamplePage(driver)
    page.open_web_form()

    controls = page.form_controls()

    assert len(controls) >= 5


def test_can_type_clear_click_and_read_element_state(driver):
    page = ExamplePage(driver)
    page.open_web_form()

    text_input = page.text_input()
    text_input.send_keys("first value")
    # Wartość pola input czyta się przez get_attribute("value").
    # `.text` zwraca textContent znacznika, a <input> nie ma tekstu w środku — byłoby puste.
    assert text_input.get_attribute("value") == "first value"

    text_input.clear()
    text_input.send_keys("final value")
    assert text_input.get_attribute("value") == "final value"

    checkbox = page.checkbox()
    # Selenium używa is_selected() dla checkbox / radio / option — nie ma metody is_checked().
    was_selected = checkbox.is_selected()
    checkbox.click()
    # `is not` zamiast `!=` jest używane, bo porównujemy dwie wartości typu bool
    # (True / False), a dla bool i innych singletonów Pythona idiomatycznie używa
    # się `is` / `is not`. Dla początkującego `!= was_selected` zadziałałoby
    # tutaj tak samo — pisz tak, jak ci wygodnie.
    assert checkbox.is_selected() is not was_selected

    assert page.disabled_input().is_enabled() is False
