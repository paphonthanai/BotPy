MyCient = "nonamename"
MyEmail = "teerawut_name@hotmail.com"
MyPassWord = "1549900401771Name" 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class Instargram:
    def __init__(self,username,password) :
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
    
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(options=options)
        self.BaseUrl = "https://www.instagram.com/"
        
    def Login(self):
        self.driver.get(f"{self.BaseUrl}accounts/login/")
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password + Keys.ENTER)
        time.sleep(8)
        self.driver.find_elements(By.XPATH,"//button[contains(text(),'Not Now')]")[0].click()
    
    def Nav_user(self,user):
        self.driver.get(f"{self.BaseUrl}{user}")
        
    def Search_Tag(self,hashtag):
        time.sleep(1)
        self.driver.get(f"{self.BaseUrl}explore/tags/{hashtag}")
        
        
    def Like_photo(self):
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME,'_aabd').click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME,'_aamw').click()
        
        
        
MYBOT = Instargram(MyEmail,MyPassWord)
MYBOT.Login()
# MYBOT.Nav_user(MyCient)
MYBOT.Search_Tag("Computer")
MYBOT.Like_photo()
