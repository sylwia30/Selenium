from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/Waits.html')
driver.set_window_size(1200, 1800)

# 1. time.sleep() - nie jest rekomandowane używania takiego rozwiazania
driver.find_element_by_id('clickOnMe').click()
# zatrzymaie egzekucji całego kodu na 5 sekund
time.sleep(5)
print(driver.find_element_by_tag_name('p').text)
driver.quit()

# 2. Implicit waits

# Implicit waits jest przypisane globalnie do każdego uruchomienia find_element_by
# wystarczy jedna linijka implicitly_wait() która obsługuje wszystkie przypadki wyszukiwania elementów
# co jest również minusem pownieważ innych akcji nie obsłuży

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/Waits.html')
driver.find_element_by_id('clickOnMe').click()
print(driver.find_element_by_tag_name('p').text)
driver.quit()

# # wprowadziliśmy niepoprawna id elementu 'clickOnMe1' które nie istnieje na stronie,
# # w tym przypadku nastąpi odczekanie 10 sekund i otrzymamy błąd NoSuchElementException,
# # selenium nie będzie mogło znależć elementu na stronie
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
# driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/Waits.html')
# driver.find_element_by_id('clickOnMe1').click()
# print(driver.find_element_by_tag_name('p').text)
# driver.quit()

# 3a. Explicit wait - WebDriverWait
# zdefiniowanie warunku na oczekiwany element
driver = webdriver.Chrome(ChromeDriverManager().install())
# przez 10 sekund i co pół sekundy system będzie sprawdzał czy element znajduje się na stronie
# można dodać wyjątek ignored_exceptions, ale nie trzeba
wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5, ignored_exceptions=NoSuchElementException)
driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/Waits.html')
driver.find_element_by_id('clickOnMe').click()
wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, 'p')))
print(driver.find_element_by_tag_name('p').text)
driver.quit()

# 3b. Explicit wait - WebDriverWait - z własnym warunkiem
driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5, ignored_exceptions=NoSuchElementException)
driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/Waits.html')
driver.find_element_by_id('clickOnMe').click()
wait.until(lambda i: len(i.find_elements_by_tag_name('p')) == 1)
print(driver.find_element_by_tag_name('p').text)
driver.quit()