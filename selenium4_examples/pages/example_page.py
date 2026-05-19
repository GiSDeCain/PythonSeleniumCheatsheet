"""Example Page Object written with Selenium 4 locator tuples."""

from selenium.webdriver.common.by import By

from selenium4_examples.pages.base_page import BasePage


WEB_FORM_URL = "https://www.selenium.dev/selenium/web/web-form.html"
THE_INTERNET_URL = "https://the-internet.herokuapp.com/"
ADD_REMOVE_URL = "https://the-internet.herokuapp.com/add_remove_elements/"

TEXT_INPUT = (By.ID, "my-text-id")
PASSWORD_INPUT = (By.NAME, "my-password")
TEXTAREA = (By.XPATH, "//textarea[@name='my-textarea']")
SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
FORM_CONTROLS = (By.CSS_SELECTOR, ".form-control")
CHECKBOX = (By.ID, "my-check-1")
DISABLED_INPUT = (By.NAME, "my-disabled")
PAGE_HEADING = (By.TAG_NAME, "h1")
ADD_REMOVE_LINK = (By.LINK_TEXT, "Add/Remove Elements")
PARTIAL_LINK = (By.PARTIAL_LINK_TEXT, "Selenium")
BUTTON_CLASS = (By.CLASS_NAME, "btn")


class ExamplePage(BasePage):
    """Minimal Page Object used by the Selenium 4 tests."""

    def open_web_form(self):
        self.open(WEB_FORM_URL)

    def text_input(self):
        return self.find(TEXT_INPUT)

    def password_input(self):
        return self.find(PASSWORD_INPUT)

    def textarea(self):
        return self.find(TEXTAREA)

    def submit_button(self):
        return self.find(SUBMIT_BUTTON)

    def form_controls(self):
        return self.find_all(FORM_CONTROLS)

    def checkbox(self):
        return self.find(CHECKBOX)

    def disabled_input(self):
        return self.find(DISABLED_INPUT)

    def heading(self):
        return self.find(PAGE_HEADING)

    def submit(self):
        self.submit_button().click()
