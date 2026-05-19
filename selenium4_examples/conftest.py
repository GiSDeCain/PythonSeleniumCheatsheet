"""Pytest setup for Selenium 4 examples."""

import os
from pathlib import Path

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


WINDOW_SIZE = "1280,900"
SELENIUM_MAJOR_VERSION = selenium.__version__.split(".", maxsplit=1)[0]
EXAMPLES_ROOT = Path(__file__).parent.resolve()


# Uwaga dydaktyczna: poniższa funkcja to tzw. hook pytest. Pytest sam ją wywoła
# po zebraniu listy testów. Zadanie hooka: jeśli mentee odpali pytest w złym
# virtualenvie (Selenium 3 zamiast 4), oznacz testy jako skipped z czytelnym
# komunikatem zamiast wybuchać niezrozumiałym ImportError.
# To jest "pytest-magic" — nie musisz rozumieć tego kodu linijka po linijce,
# żeby pisać własne testy. Patrz README, sekcja "Mechanizm skip drugiej wersji".
def pytest_collection_modifyitems(items):
    """Skip Selenium 4 examples when the active virtualenv has Selenium 3."""
    if SELENIUM_MAJOR_VERSION == "4":
        return

    skip = pytest.mark.skip(
        reason="Selenium 4 examples require selenium==4.x. Use requirements-selenium4.txt."
    )
    for item in items:
        if Path(str(item.fspath)).resolve().is_relative_to(EXAMPLES_ROOT):
            item.add_marker(skip)


def build_chrome_options():
    """Create ChromeOptions in the Selenium 4 style."""
    options = webdriver.ChromeOptions()
    options.add_argument(f"--window-size={WINDOW_SIZE}")

    # `os.getenv("HEADLESS", "")` zwraca wartość zmiennej środowiskowej HEADLESS
    # albo pusty string, jeśli zmienna nie jest ustawiona. `.lower()` ujednolica
    # wielkość liter, a `in {"1", "true", "yes"}` sprawdza, czy wartość jest na
    # liście "uznawanych za włączone". Dzięki temu działa zarówno HEADLESS=1,
    # jak i HEADLESS=true czy HEADLESS=YES.
    if os.getenv("HEADLESS", "").lower() in {"1", "true", "yes"}:
        options.add_argument("--headless=new")

    return options


@pytest.fixture
def driver():
    """Start and close Chrome for every test.

    In Selenium 4, webdriver.Chrome(options=options) can use Selenium Manager.
    If CHROMEDRIVER_PATH is set, the explicit Service(...) style is shown instead.
    """
    options = build_chrome_options()
    chromedriver_path = os.getenv("CHROMEDRIVER_PATH")

    if chromedriver_path:
        browser = webdriver.Chrome(
            service=Service(chromedriver_path),
            options=options,
        )
    else:
        browser = webdriver.Chrome(options=options)

    try:
        yield browser
    finally:
        browser.quit()
