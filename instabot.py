from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self,username, pwd):
        self.driver = webdriver.Chrome()
        #self.driver.get("https://www.instagram.com")
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        self.username = username
        self.pwd = pwd
        sleep(2)
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/p/a').click()
        #self.driver.find_element_by_xpath("//a[contains(text(), 'Connectez-vous')]").click()
        #sleep(2)
        #login field
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        #password field
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pwd)
        #login
        
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(2)

        #self.driver.find_element_by_xpath("//a[contains(text(), 'Plus tard')]").click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(2)


    def unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]").click()
        sleep(1)
        #self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        #suggestions = self.driver.find_elements_by_xpath("//h4[contains(text(), Suggestions)]")
        #self.driver.execute_script('arguments[0].scrollIntoView()', suggestions)
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight; """, scroll_box)



bot = InstaBot('artyboy420', 'artyboy')
bot.unfollowers()