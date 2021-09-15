import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def seleniumScrap(url, browser, dic):
    # Open url in navigator
    browser.get(url)
    time.sleep(6) # Time lapse test 6 or + seconds
    #browser.implicitly_wait(6)
    # Obtain elements acording to class
    name = browser.find_element_by_class_name('CSS-CLASS')

    dic[name] = name

option = webdriver.ChromeOptions()
# second plane browser option
option.add_argument("headless")
browser = webdriver.Chrome(chrome_options=option)

product_price = {}
links = ["URL"]

for url in links:
    seleniumScrap(url,browser,product_price)

# Close Browser and show dictionary
browser.quit()
print(product_price)