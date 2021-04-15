from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/Test.html')
driver.set_window_size(1000, 1200)

driver.execute_script('arguments[0].click();', driver.find_element_by_id('clickOnMe'))
driver.switch_to.alert.accept()

value = 'Anna'
driver.execute_script("arguments[0].setAttribute('value', '" + value + "')", driver.find_element_by_id('fname'))

driver.quit()