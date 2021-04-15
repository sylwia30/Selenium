from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///home/sylwia/dev/workr_sylwia/Udemy_Selenium/materialy_wykorzystywane_w_kodzie/Test.html')
driver.set_window_size(1000, 1200)

# 1. lokalizowanie elementów
# <button type="button" id="clickOnMe" onclick="alert('Hello world!')">Kliknij mnie!</button>
driver.find_element_by_id('clickOnMe')
driver.find_element(By.ID, 'clickOnMe')

# <input type="text" name="fname" id="fname">
driver.find_element_by_name('fname')

# <a href="https://www.w3schools.com">Visit W3Schools.com!</a>
driver.find_element_by_link_text('Visit W3Schools.com!')
# wyszukiwanie po niepełnej tresci link tekstu
driver.find_element_by_partial_link_text('Visit W3Schools')

# <p class="topSecret" hidden="">This paragraph should be hidden.</p>
driver.find_element_by_class_name('topSecret')

# 3 wyszukiwanie po tagach
driver.find_element_by_tag_name('a')
driver.find_element_by_tag_name('p')
driver.find_element_by_tag_name('label')

# <img id="smileImage" src="smile.png">
# wyszukiwanie po selectorze i jego id, dodajemy # przed wartoscia id: #id
driver.find_elements_by_css_selector('img#smileImage')

# <p class="topSecret" hidden="">This paragraph should be hidden.</p>
# wyszukiwanie po selectorze i jego klasie, dodajemy . przed wartoscia klasy: .classmane
driver.find_elements_by_css_selector('p.topSecret')

# <table border="1">
#   <tbody><tr>
#     <th class="tableHeader">Month</th>
#     <th class="tableHeader">Savings</th>
#   </tr>
#   <tr>
#     <td>January</td>
#     <td>$100</td>
#   </tr>
# </tbody></table>

print(driver.find_element_by_css_selector('th:first-child').text)
# Month
print(driver.find_element_by_css_selector('th:nth-child(1)').text)
# Month
print(driver.find_element_by_css_selector('th:last-child').text)
# Savings
print(driver.find_element_by_css_selector('th:nth-child(2)').text)
# Savings
print(driver.find_element_by_css_selector('td:first-child').text)
# January

# lokalizowanie elementow za pomocą XPath

# <html>
#     <body>
#         <h1>Witaj na stronie testowej</h1>
#         <button type="button" id="clickOnMe" onclick="alert('Hello world!')">Kliknij mnie!</button> <br>
#         <label for="fname"> First name:</label> <br>
#         <input type="text" name="fname" id="fname"><br>
#         <a href="https://www.w3schools.com">Visit W3Schools.com!</a> <br>
#         <a href="https://www.google.com">IamWeirdLink</a> <br>
#         <table border="1">
#           <tr>
#                 <th class="tableHeader">Month</th>
#                 <th class="tableHeader">Savings</th>
#           </tr>
#           <tr>
#                 <td>January</td>
#                 <td>$100</td>
#           </tr>
#         </table>
#     </body>
# </html>

# ścieżka relatywna od początku DOM aby otrzymać elemen th w tabeli
driver.find_element_by_xpath('/html/body/table/tbody/tr/th')

# podwójny ukośnik wyszukuje element od pewnego momentu jaki okreslimy w sciezce
driver.find_element_by_xpath('//table/tbody/tr/th')
print(driver.find_element_by_xpath('//table/tbody/tr/th').text)

driver.find_element_by_xpath('//th')

# wyszukiwanie po tekście
driver.find_element_by_xpath('//th[text()="Month"]')

# wyszukiwanie po atrybucie name, używamy @
# <input type="text" name="fname" id="fname"><br>
driver.find_element_by_xpath('//input[@name="fname"]')

# wyszukiwanie po id, używamy @
# <input type="text" name="fname" id="fname"><br>
driver.find_element_by_xpath('//input[@id="fname"]')

# <button type="button" id="clickOnMe" onclick="alert('Hello world!')">Kliknij mnie!</button> <br>
driver.find_element_by_xpath('//button[@id="clickOnMe"]')

# używając /.. przechodzimy do parenta powyżej (elementu nadżednego) w tym przypadku do body
driver.find_element_by_xpath('//input[@name="fname"]/..')

# używając /following-siblings:: szukamy tagu ktory znajduje się na takim samym poziomie
driver.find_element_by_xpath('//input[@id="fname"]/following-sibling::button')
print(driver.find_element_by_xpath('//input[@id="fname"]/following-sibling::button').text)
# output: Click me tj. nazwa buttona

# po skopiowaniu ścieżki xpath z poziomu 'Inspect' przeglądarki możemy otrzymać taką ścieżkę:
# //*[@id="clickOnMe"]
# gwiazdka oznacza jaki kolwiek selector, co nie jest bezpieczne dlatego można zawęzić wyszukiwanie
# zamieniając * na konkretny element tj. w tym przypadku button
# //button[@id="clickOnMe"]

# lokalizowanie wielu elementów
lista_elementów = driver.find_elements_by_xpath('//th')
print(len(lista_elementów))
# output: 2

driver.quit()


