from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/')

# manualne ustawianie wielkosci przegladarki
driver.set_window_size(1800, 1200)
print(driver.get_window_size())

# automatyczne ustawianie wielkości przeglądarki, nie zaleca się z racji różnej wielkości rozdzielczości komputerów
driver.maximize_window()
print(driver.get_window_size())

driver.minimize_window()
print(driver.get_window_size())

driver.fullscreen_window()

