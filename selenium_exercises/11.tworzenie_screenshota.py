from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(1000, 1200)
driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/FileUpload.html')

driver.save_screenshot('screenshots/screenshot_1.png')