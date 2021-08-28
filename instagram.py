import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from insta_info import username, password, person, msg


class Instagram:
    def __init__(self, username, password, person, msg):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs", {"intl.accept_languages":"en,en_US"})
        self.browser = webdriver.Chrome("chromedriver.exe", chrome_options=self.browserProfile)
        self.username = username
        self.password = password
        self.person = person
        self.msg = msg

    def sign_in(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def save(self):
        self.browser.get("https://www.instagram.com/accounts/onetap/?next=%2F")
        time.sleep(1)
        notnow = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        notnow.click()
        time.sleep(1)

    def notifications(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(1)
        notnow2 = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notnow2.click()
        time.sleep(1)

    def dm(self):
        self.browser.get(f"https://www.instagram.com/{person}")
        time.sleep(2)
        open = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button')
        open.click()
        time.sleep(8)
        box = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        box.send_keys(msg)
        time.sleep(2)
        box.send_keys(Keys.ENTER)


insta = Instagram(username, password, person, msg)
insta.sign_in()
insta.save()
insta.notifications()
insta.dm()
