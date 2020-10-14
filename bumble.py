from selenium import webdriver
from time import sleep

class BumbleBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://bumble.com/get-started')

        sleep(2)

        clickbutton = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div')
        clickbutton.click()

        base_window = self.driver.window_handles[0]
        popup = self.driver.switch_to.window(bot.driver.window_handles[1])

        sleep(1)
        email = self.driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys('alimbetov.m@mail.ru')

        sleep(1)
        password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys('barcamuxa18')

        login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login.click()
        sleep(3)

        self.driver.switch_to.window(base_window)

        sleep(3)

        while True:
            sleep(2)
            like_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div')
            like_btn.click()




bot = BumbleBot()
bot.login()



