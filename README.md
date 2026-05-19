# Selenium Mentee Cheatsheet

Edukacyjny projekt demonstracyjny dla osób uczących się automatyzacji testów frontendu w Pythonie.

Projekt pokazuje podstawy Selenium na dwóch ścieżkach:

- `selenium3_examples/` - historyczny styl Selenium 3, spotykany w starszych projektach.
- `selenium4_examples/` - aktualny styl Selenium 4, rekomendowany do nowych projektów.

To nie jest framework enterprise. To ma być czytelna ściąga: krótkie testy, proste Page Objecty i komentarze tylko tam, gdzie pomagają zrozumieć mechanizm albo różnicę między wersjami.

## Wymagania

- Python 3.10+
- Google Chrome
- ChromeDriver zgodny z lokalną wersją Chrome
- Dostęp do internetu, bo testy używają publicznych stron demonstracyjnych:
  - `https://www.selenium.dev/selenium/web/web-form.html`
  - `https://the-internet.herokuapp.com/`

## Ważne: osobne środowiska

Selenium 3 i Selenium 4 to różne wersje tego samego pakietu `selenium`, dlatego najczytelniej uruchamiać je w osobnych virtualenvach.

## Instalacja dla Selenium 3

Selenium 3 nie ma Selenium Managera. Musisz mieć lokalny `chromedriver` dostępny w `PATH` albo wskazać go przez `CHROMEDRIVER_PATH`.

> Uwaga o kompatybilności: `selenium==3.141.0` realnie współpracuje z Chrome / ChromeDriverem do mniej więcej wersji 114. Na świeżym Chrome 115+ pojawiają się błędy startu sesji albo niedopasowania protokołu. Jeżeli masz nowszego Chrome'a zainstalowanego systemowo, do ścieżki Selenium 3 użyj pinowanej pary Chrome + ChromeDriver z [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/) (np. 114) i wskaż ją przez `CHROMEDRIVER_PATH`. Selenium 4 nie ma tego problemu.

```bash
python3 -m venv .venv-selenium3
source .venv-selenium3/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-selenium3.txt
```

Jeżeli `chromedriver` nie jest w `PATH`:

```bash
export CHROMEDRIVER_PATH=/sciezka/do/chromedriver
```

Uruchomienie testów Selenium 3 (zawsze z katalogu głównego repo):

```bash
pytest selenium3_examples/tests
```

## Instalacja dla Selenium 4

Selenium 4 potrafi użyć Selenium Managera, który w nowszych wersjach automatycznie dobiera i pobiera driver przeglądarki.

```bash
python3 -m venv .venv-selenium4
source .venv-selenium4/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-selenium4.txt
```

Uruchomienie testów Selenium 4 (zawsze z katalogu głównego repo):

```bash
pytest selenium4_examples/tests
```

Jeżeli chcesz wymusić konkretny ChromeDriver:

```bash
export CHROMEDRIVER_PATH=/sciezka/do/chromedriver
pytest selenium4_examples/tests
```

## Skąd uruchamiać `pytest`

Testy muszą być uruchamiane **z katalogu głównego repo** (tam, gdzie leży `pytest.ini`). Importują Page Objecty przez ścieżki w stylu `from selenium3_examples.pages.example_page import ...`, a te ścieżki są widoczne tylko wtedy, gdy `pytest` startuje z roota. Wejście do `selenium3_examples/tests/` i odpalenie `pytest` skończy się `ModuleNotFoundError`.

## Markery pytest

Każdy plik testowy jest oznaczony markerem (`selenium3` albo `selenium4`) — zarejestrowane w `pytest.ini`. Można dzięki temu uruchomić tylko jedną grupę:

```bash
pytest -m selenium4
pytest -m selenium3
```

Bez `-m` pytest puszcza wszystko, co znajdzie w `testpaths`.

## Skipowany test antywzorca

W `selenium3_examples/tests/test_waits.py` i `selenium4_examples/tests/test_waits.py` znajdziesz po jednym teście z `@pytest.mark.skip`. To nie jest popsuty test — to celowo pokazany **antywzorzec z `time.sleep`**, żeby mentee zobaczył, jak nie pisać oczekiwań. Output `pytest` pokaże go jako `skipped`, to jest oczekiwane.

## Mechanizm "skip drugiej wersji" w `conftest.py`

W obu `conftest.py` jest funkcja `pytest_collection_modifyitems`. To jest hook pytest — uruchamia się raz po zebraniu listy testów i sprawdza, którą wersję `selenium` masz aktywną w virtualenvie. Jeżeli aktywne jest Selenium 4, a próbujesz odpalić testy z `selenium3_examples/`, hook automatycznie skipuje je z czytelnym komunikatem (i odwrotnie). To jest "pytest-magic", **nie musisz rozumieć tego kodu, żeby używać projektu** — wystarczy że wiesz, czemu czasem widzisz `skipped`.

## Headless Chrome

Domyślnie testy otwierają normalne okno Chrome, co jest wygodne podczas nauki. Tryb headless można włączyć tak:

```bash
export HEADLESS=1
pytest selenium4_examples/tests
```

## Różnice Selenium 3 vs Selenium 4 w skrócie

Selenium 3 pokazuje historyczne API:

```python
driver = webdriver.Chrome(executable_path="chromedriver", options=options)
element = driver.find_element_by_css_selector("button")
```

Selenium 4 używa aktualnego API:

```python
driver = webdriver.Chrome(options=options)
element = driver.find_element(By.CSS_SELECTOR, "button")
```

W Selenium 4 lokatory są jawnie przekazywane przez klasę `By`, a konfigurację ścieżki do drivera robi się przez `Service`.

## Rekomendowana kolejność nauki

1. Inicjalizacja drivera.
2. Nawigacja: `get`, `title`, `current_url`, `back`, `forward`, `refresh`.
3. `find_element` i `find_elements`.
4. Lokatory: ID, name, CSS, XPath, link text.
5. Akcje na elementach: `click`, `send_keys`, `clear`.
6. Odczyt stanu: `text`, `get_attribute`, `is_displayed`, `is_enabled`, `is_selected`.
7. `WebDriverWait`.
8. `expected_conditions`.
9. Typowe wyjątki Selenium.
10. Page Object Pattern.

## Struktura

```text
.
  README.md
  AGENTS.md
  requirements-selenium3.txt
  requirements-selenium4.txt
  pytest.ini

  selenium3_examples/
    conftest.py
    pages/
      base_page.py
      example_page.py
    tests/
      test_basic_browser.py
      test_find_elements.py
      test_waits.py
      test_error_handling.py

  selenium4_examples/
    conftest.py
    pages/
      base_page.py
      example_page.py
    tests/
      test_basic_browser.py
      test_find_elements.py
      test_waits.py
      test_error_handling.py

  docs/
    selenium3_vs_4.md
    locators_cheatsheet.md
    waits_cheatsheet.md
    common_exceptions.md
```

## Dokumentacja

- `docs/selenium3_vs_4.md` - główne różnice między Selenium 3 i 4.
- `docs/locators_cheatsheet.md` - ściąga z lokatorów.
- `docs/waits_cheatsheet.md` - jawne czekanie i expected conditions.
- `docs/common_exceptions.md` - typowe wyjątki i sposoby reagowania.
