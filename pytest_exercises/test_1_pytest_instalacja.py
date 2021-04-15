# pip install pytest

import pytest


def test_method():
    x = 2
    y = 3
    assert x + y == 5, 'Assertion failed, expected 5'
    assert x + y == 2, 'Assertion failed, expected 2'

# uruchamiamy test w terminalu uzywając komendy:
# uruchomienie wszystkich plików z testami:
# pytest

# uruchomienie konkternego pliku w terminalu z testami:
# pytest test_1_pytest_instalacja.py

# uruchomienie testu z poziomu PyCharma
# Settings -> Tools -> Python Integrated Tools
# w sekcji Testing, w polu Default test runner ustawiamy wartosc: pytest

# Uwaga!
# pliki które mają w nazwie test z '_' niezależnie od umiejscowienia uruchomią się podczas testów
# metody jednak musza zaczynać się od słowa 'test_' w innym wypadku nie zostaną uruchomione