from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/Test.html')
driver.set_window_size(1200, 1800)

# 1. klikanie na element
# driver.find_element_by_id('clickOnMe').click()

# 2. obsługa alertów na stronie
# driver.find_element_by_id('clickOnMe').click()
# driver.find_element_by_id('clickOnMe').click()

# podwójny klik na stronie powoduje błąd w postaci:
# selenium.common.exceptions.UnexpectedAlertPresentException: Alert Text: Hello world!

# obsługa alertu:
driver.find_element_by_id('clickOnMe').click()
# system automatycznie akceptuje błąd
driver.switch_to.alert.accept()

driver.find_element_by_id('clickOnMe').click()
# system automatycznie ignoruje błąd
driver.switch_to.alert.dismiss()

# 3. wprowadzanie wartości do pola tesktowego
driver.find_element_by_id('fname').send_keys('Sylwia')

# 4. Symulacja naciśnięcia przycisku Enter
driver.find_element_by_name('password').send_keys(Keys.ENTER)
driver.switch_to.alert.accept()
driver.switch_to.alert.accept()

# 5. wybanie elementu z listy rowijanej select
auto_select = Select(driver.find_element_by_tag_name('select'))
auto_select.select_by_visible_text('Volvo')
# <option value="mercedes">Mercedes</option>
auto_select.select_by_value('mercedes')
auto_select.select_by_index(1)

# 6. zaznaczanie checkboxa
driver.find_element_by_xpath('//input[@type="checkbox"]').click()

# 7. zaznaczanie radio buttona
driver.find_element_by_xpath('//input[@value="male"]').click()

# 8. pobieranie tekstu z elementu
print(driver.find_element_by_tag_name('h1').text)
print(driver.find_element_by_id('clickOnMe').text)

# pobieranie tekstu z inputa
print('test inputa to: ' + driver.find_element_by_id('fname').text)
# jak widać tekst nie jest widoczny
print('test inputa to: ' + driver.find_element_by_xpath('//input[@name="username"]').get_attribute('value'))

# 9. Pobieranie tekstu z ukrytego elementu 'hidden'
# <p hidden="" class="topSecret">This paragraph should be hidden.</p>
print(driver.find_element_by_tag_name('p').text)
# jak widać test nie jest dla nas widoczny
print(driver.find_element_by_tag_name('p').get_attribute('textContent'))

# 10. Sprawdzenie czy obrazek wyświetla się na stronie

# brak wyświetlanego obrazka, na stronie widoczna jest ikona braku obrazka
# <img id="smileImage1" src="test.png">
print(driver.find_element_by_id('smileImage1').size)
# output: {'height': 16, 'width': 16}
obrazek = driver.find_element_by_id('smileImage1').get_attribute('naturalHeight')
# output: 0
# 0 oznacza że obrazek nie jest widoczny na stronie

# obrazek wyświetla się prawidłowo
# <img id="smileImage1" src="smile.png">
obrazek = driver.find_element_by_id('smileImage2').get_attribute('naturalHeight')
print(obrazek)
# output: 223
assert int(obrazek) > 0


# 11. Przełączanie do nowo otwartego okna przeglądarki

driver.find_element_by_id('newPage').click()
print(driver.title)
# outupt: Strona testowa

# aktualne okno:
current_window_name = driver.current_window_handle
# lista dostępnych okien
window_names = driver.window_handles
print(window_names)
# outupt: ['CDwindow-5AB7DBA824589E63D2FEFA74B85D5B52', 'CDwindow-DF09AD01AD8D137C3F940CD720FED0BC']

for window in window_names:
    if window != current_window_name:
        driver.switch_to.window(window)

print(driver.title)
# output: Google

driver.switch_to.window((current_window_name))
print(driver.title)

# 12. Nadpisywanie inputa

driver.find_element_by_name('username').send_keys('Agata')

# 13. usuwanie wartości z inputa i wprowadzenie nowej wartości

driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys('Lukasz')