from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/Test.html')

# klikamy na element otwierajacy nowa strone google
driver.find_element_by_id('newPage').click()

# zamkniecie strony Test, strona google jest nadal widoczna
driver.close()

# zmkniecie wszystkich stron
driver.quit()

