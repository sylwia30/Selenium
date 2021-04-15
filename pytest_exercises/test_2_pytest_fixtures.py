import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture() dodanie dekoratora fixture oznacza, że metoda ta zostanie uruchomiona podczas testu,
# musimy jednak dodać parametr tej metody w metodzie testowej aby została uruchomiona


@pytest.fixture()
def test_setup_driver():
    # zmienna globalna dostępna w innych metodach
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/Test.html')
    driver.set_window_size(1200, 1800)
    # yield zostanie wywołany na końcu danego testu i zamknie przeglądarkę
    yield
    driver.quit()


def test_title_browser(test_setup_driver):
    assert driver.title == 'Strona testowa'

