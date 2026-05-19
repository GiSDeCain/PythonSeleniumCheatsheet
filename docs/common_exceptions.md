# Common Selenium Exceptions

## NoSuchElementException

Selenium nie znalazł elementu dla podanego lokatora.

Typowe przyczyny:

- Zły lokator.
- Element jest na innej stronie.
- Element pojawia się dopiero po czasie.
- Test szuka elementu w złym iframe.

Typowa reakcja:

```python
wait.until(EC.visibility_of_element_located((By.ID, "login")))
```

## TimeoutException

Warunek w `WebDriverWait` nie został spełniony w podanym czasie.

Typowe przyczyny:

- Aplikacja działa wolniej niż założono.
- Warunek jest źle dobrany.
- Lokator jest błędny.
- Po akcji nie nastąpił oczekiwany efekt.

Typowa reakcja: sprawdź lokator, warunek i realne zachowanie strony.

## StaleElementReferenceException

Referencja do elementu jest nieaktualna, bo DOM został przeładowany albo element został wyrenderowany ponownie.

Typowy błąd:

```python
button = driver.find_element(By.CSS_SELECTOR, "button")
driver.refresh()
button.click()
```

Typowa reakcja: znajdź element ponownie po zmianie DOM.

## ElementClickInterceptedException

Selenium próbował kliknąć element, ale kliknięcie zostało przechwycone przez inny element.

Typowe przyczyny:

- Modal zasłania przycisk.
- Baner cookies zasłania element.
- Loader jest jeszcze widoczny.
- Element jest poza widoczną częścią strony.

Typowa reakcja:

```python
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))
button.click()
```

Jeżeli problemem jest modal lub baner, test powinien najpierw go zamknąć albo poczekać, aż zniknie.
