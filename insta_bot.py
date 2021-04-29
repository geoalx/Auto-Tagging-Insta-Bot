from selenium import webdriver
from time import sleep
import random

class InstaBot:
    def __init__(self):
        with open("credentials.txt") as f:
            s = f.readlines()
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(3)
        usr = self.driver.find_element_by_name("username")
        psw = self.driver.find_element_by_name("password")
        usr.send_keys(s[0])
        psw.send_keys(s[1])
        psw.submit()
        sleep(5)
        #self.driver.quit()

    def comment(self):
        users = []
        with open("credentials.txt") as f:
            s = f.readlines()
            users = s[3].split(",")
        flag = True
        self.driver.get(s[2])
        sleep(5)
        while(flag):
            try:
                el_txt = self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
                el_txt.click()
                el_txt = self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
                el_txt.send_keys(users[random.randint(0,int(len(users)/3))] + " "+users[random.randint(int(len(users)/3+1),int(2*len(users)/3))] + " "+users[random.randint(int(2*len(users)/3+1),len(users)-1)])
                send = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]")
                send.click()
                print("commented")
                sleep(random.randint(60,180))
            except:
                print("PROCCESS STOPPED")
                flag = False

I = InstaBot()
I.comment()
