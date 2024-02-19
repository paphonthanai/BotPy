from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("http://www.facebook.com")


# driver = webdriver.Chrome()
# str1 = driver.capabilities['browserVersion']
# str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
# print(str1)
# print(str2)
# print(str1[0:2])
# print(str2[0:2])
# if str1[0:2] != str2[0:2]: 
#   print("please download correct chromedriver version")