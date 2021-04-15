import webdriver_manager.driver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/Test.html')


# 1. sprawdzanie czy element is_enabled
# np. czy użytkownik może wprowadzić wartość do inputa

first_name = driver.find_element_by_id('fname')
if first_name.is_enabled():
    first_name.send_keys('Sylwia')
else:
    print('Element is not enabled')

last_name = driver.find_element_by_id('lname')

if last_name.is_enabled():
    last_name.send_keys('Sylwia')
else:
    print('Element is disabled')

# 2. sprawdzanie czy element is_displayed
# np. czy element jest widoczny czy tez ukryty 'hidden' w html-u

# <p hidden class="topSecret">This paragraph should be hidden.</p>
# <p class="notSecret">Second paragraph should be visible.</p>

hidden_paragraf = driver.find_element_by_class_name('topSecret')
visible_paragraf = driver.find_element_by_class_name('notSecret')

print('hidden paragraf:')
if hidden_paragraf.is_displayed():
    print(hidden_paragraf.text)
else:
    print('Is not displayed')
    # pobieramy nazwę atrybutu ukrytego taga
    print(hidden_paragraf.get_attribute('textContent'))


print('visible paragraf:')

if visible_paragraf.is_displayed():
    print(visible_paragraf.text)
else:
    print('Is not displayed')
    print(visible_paragraf.get_attribute('textContent'))

# 3. sprawdzanie czy element isnieje na stronie
    # czy istnieje na stronie

# metoda pierwsza za pomocą try except.
try:
    driver.find_element_by_tag_name('abc')
except NoSuchElementException:
    print('element nie istnieje')

# metoda druga za pomocą len(). Element jest widoczny nawet jak jest 'hidden'
element = driver.find_elements_by_class_name('topSecret')

if len(element) > 0:
    print('element istnieje')
else:
    print('element nie istnieje')

# 3. Sprawdzenie czy element jest wybrany/zaznaczony is_selected
# is_selected zwraca wartość True/False

checkbox = driver.find_element_by_xpath('//input[@type="checkbox"]')
print(checkbox.is_selected())

if checkbox.is_selected():
    print('Wartość zaznaczona. Odznaczam!')
    checkbox.click()
else:
    print('Zaznaczam checkbox')
    checkbox.click()
    
print(checkbox.is_selected())


driver.quit()



