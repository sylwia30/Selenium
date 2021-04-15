from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/iFrameTest.html')
driver.set_window_size(1200, 1800)
print(driver.find_element_by_tag_name('h1').text)
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
print(driver.find_element_by_tag_name('h1').text)
driver.switch_to.default_content()
print(driver.find_element_by_tag_name('h1').text)
driver.quit()