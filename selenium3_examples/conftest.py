"""Pytest setup for Selenium 3 examples."""

import os
from pathlib import Path

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


WINDOW_SIZE = "1280,900"
DEFAULT_CHROMEDRIVER = "chromedriver"
SELENIUM_MAJOR_VERSION = selenium.__version__.split(".", maxsplit=1)[0]
EXAMPLES_ROOT = Path(__file__).parent.resolve()


# Uwaga dydaktyczna: poniższa funkcja to tzw. hook pytest. Pytest sam ją wywoła
# po zebraniu listy testów. Zadanie hooka: jeśli mentee odpali pytest w złym
# virtualenvie (Selenium 4 zamiast 3), oznacz testy jako skipped z czytelnym
# komunikatem zamiast wybuchać niezrozumiałym ImportError.
# To jest "pytest-magic" — nie musisz rozumieć tego kodu linijka po linijce,
# żeby pisać własne testy. Patrz README, sekcja "Mechanizm skip drugiej wersji".
def pytest_collection_modifyitems(items):
    """Skip Selenium 3 examples when the active virtualenv has Selenium 4."""
    if SELENIUM_MAJOR_VERSION == "3":
        return

    skip = pytest.mark.skip(
        reason="Selenium 3 examples require selenium==3.x. Use requirements-selenium3.txt."
    )
    for item in items:
        if Path(str(item.fspath)).resolve().is_relative_to(EXAMPLES_ROOT):
            item.add_marker(skip)


def build_chrome_options():
    """Create ChromeOptions in the Selenium 3 style."""
    options = Options()
    options.add_argument(f"--window-size={WINDOW_SIZE}")

    # `os.getenv("HEADLESS", "")` zwraca wartość zmiennej środowiskowej HEADLESS
    # albo pusty string, jeśli zmienna nie jest ustawiona. `.lower()` ujednolica
    # wielkość liter, a `in {"1", "true", "yes"}` sprawdza, czy wartość jest na
    # liście "uznawanych za włączone". Dzięki temu działa zarówno HEADLESS=1,
    # jak i HEADLESS=true czy HEADLESS=YES.
    if os.getenv("HEADLESS", "").lower() in {"1", "true", "yes"}:
        options.add_argument("--headless")

    return options


@pytest.fixture
def driver():
    """Start and close Chrome for every test.

    Selenium 3 accepted executable_path directly in webdriver.Chrome.
    This is historical API kept here on purpose for reading older projects.
    """
    chromedriver_path = os.getenv("CHROMEDRIVER_PATH", DEFAULT_CHROMEDRIVER)
    browser = webdriver.Chrome(
        executable_path=chromedriver_path,
        options=build_chrome_options(),
    )

    try:
        yield browser
    finally:
        browser.quit()
