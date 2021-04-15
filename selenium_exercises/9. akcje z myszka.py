from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(1000, 1200)
driver.get('https://www.w3schools.com/')

time.sleep(2)
window = driver.find_element_by_id('accept-choices')
window.click()

# 1. najechanie na element myszka
tutorials_tab = driver.find_element_by_id('navbtn_tutorials')
webdriver.ActionChains(driver).move_to_element(tutorials_tab).perform()

# 2. Łączenie akcji ActionChains (najechanie myszką na element i jego kliknięcie)
webdriver.ActionChains(driver).move_to_element(tutorials_tab).click().perform()
driver.quit()

# 3. przeciąanie elementów za pomocą myszki
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(1000, 1200)
driver.get('https://demos.telerik.com/kendo-ui/dragdrop/index')

# zamkniecie ciasteczek
time.sleep(2)
driver.find_element_by_id('onetrust-accept-btn-handler').click()
time.sleep(2)

# przeciągnięcie elementu
draggable_elemnet = driver.find_element_by_id('draggable')
drop_target_elemnet = driver.find_element_by_id('droptarget')
webdriver.ActionChains(driver).drag_and_drop(draggable_elemnet, drop_target_elemnet).perform()

driver.quit()
