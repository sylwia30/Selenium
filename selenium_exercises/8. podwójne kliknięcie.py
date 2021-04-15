from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/DoubleClick.html')
driver.set_window_size(1000, 1200)

# 1. podwójne kliknięcie
button = driver.find_element_by_id('bottom')

webdriver.ActionChains(driver).double_click(button).perform()

# powrót do strony głównej
current_window = driver.current_window_handle
all_windows = driver.window_handles

for window in all_windows:
    if window != current_window:
        driver.switch_to.window(window)
        driver.close()

driver.switch_to.window(current_window)

# 2. kliknięcie prawym przyciskiem myszy na element
webdriver.ActionChains(driver).context_click(button).perform()