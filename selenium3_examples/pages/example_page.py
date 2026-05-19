"""Example Page Object written with Selenium 3 locator methods."""

from selenium3_examples.pages.base_page import BasePage


WEB_FORM_URL = "https://www.selenium.dev/selenium/web/web-form.html"
THE_INTERNET_URL = "https://the-internet.herokuapp.com/"
ADD_REMOVE_URL = "https://the-internet.herokuapp.com/add_remove_elements/"

TEXT_INPUT_ID = "my-text-id"
PASSWORD_NAME = "my-password"
TEXTAREA_XPATH = "//textarea[@name='my-textarea']"
SUBMIT_BUTTON_CSS = "button[type='submit']"
FORM_CONTROL_CSS = ".form-control"
CHECKBOX_ID = "my-check-1"
DISABLED_INPUT_NAME = "my-disabled"


class ExamplePage(BasePage):
    """Minimal Page Object used by the Selenium 3 tests."""

    def open_web_form(self):
        self.open(WEB_FORM_URL)

    def text_input(self):
        return self.driver.find_element_by_id(TEXT_INPUT_ID)

    def password_input(self):
        return self.driver.find_element_by_name(PASSWORD_NAME)

    def textarea(self):
        return self.driver.find_element_by_xpath(TEXTAREA_XPATH)

    def submit_button(self):
        return self.driver.find_element_by_css_selector(SUBMIT_BUTTON_CSS)

    def form_controls(self):
        return self.driver.find_elements_by_css_selector(FORM_CONTROL_CSS)

    def checkbox(self):
        return self.driver.find_element_by_id(CHECKBOX_ID)

    def disabled_input(self):
        return self.driver.find_element_by_name(DISABLED_INPUT_NAME)

    def submit(self):
        self.submit_button().click()
