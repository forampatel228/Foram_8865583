
# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca/")
time.sleep(10)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
all_button = driver.find_element("xpath","/html/body/div[1]/header/div/div[4]/div[1]/a")
all_button.click()

time.sleep(10)
#best seller button click bt xpath
bestseller_button = driver.find_element("xpath","/html/body/div[3]/div[2]/div/ul[1]/li[2]/a")
bestseller_button.click()


time.sleep(10)
product_image =  driver.find_element("id","B01N17N0MO")
product_image.click()

time.sleep(10)

#filter button click by id
add_cart_button =  driver.find_element("id","add-to-cart-button")
add_cart_button.click()
time.sleep(10)

#go to card button click css selector
goto_cart_button = driver.find_element(By.CSS_SELECTOR, "#sw-gtc > span > a")
goto_cart_button.click()
time.sleep(10)

#proceed to checkout button click
proceed_to_checkout = driver.find_element(By.CLASS_NAME, "a-button-inner")
proceed_to_checkout.click()
time.sleep(10)


# Closing the webdriver
driver.close()
