# instalowanie selenium: pip install selenium

# 1 sposob: instalowanie drivera odpowiedniej wersji Chrome jaką mamy na komputerze,
#           żródło: https://chromedriver.chromium.org/downloads

from selenium import webdriver

driver = webdriver.Chrome(executable_path='/drivers/chromedriver')
driver.get('https://www.google.com/')

# 2 sposob: autoinstalownaie drivera po uruchomieniu kazdego testu poprzez webdriver_manager
#   pip install webdriver_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/')
