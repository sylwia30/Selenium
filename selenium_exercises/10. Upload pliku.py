from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(1000, 1200)
driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/FileUpload.html')

path = os.path.abspath('../materialy_wykorzystywane_w_kodzie/upload.txt')

upload_file = driver.find_element_by_id('myFile')

upload_file.send_keys(path)
