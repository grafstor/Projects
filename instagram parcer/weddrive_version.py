#---------------------------------#
#       author: grafstor
#       date: 02.06.2020
#---------------------------------#

__version__ = '1.0'

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pyvirtualdisplay import Display

class Parcer:
    def __init__(self, login, password, is_hide_display=False):

        self.is_hide_display = is_hide_display

        if self.is_hide_display:
            self.display = Display(visible=0, size=(800, 600))
            self.display.start()

        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        print('Authorization..')

        self.authorization(login, password)

    def authorization(self, login, password):
        self.driver.get('http://www.instagram.com/')
        time.sleep(1.3)

        auth_line = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[{}]/div/label/input'

        input_login_box = self.driver.find_element_by_xpath(auth_line.format(2))
        input_login_box.send_keys(login)

        input_password_box = self.driver.find_element_by_xpath(auth_line.format(3))
        input_password_box.send_keys(password)
        input_password_box.send_keys(webdriver.common.keys.Keys.ENTER)

        time.sleep(3)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

    def get_inst_page(self,name):
        self.driver.get(f'https://www.instagram.com/{name}/')
        time.sleep(1)

    def get_sub_subp(self):

        subscribers_num = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
        subscriptions_num = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text

        return (subscribers_num, subscriptions_num)

    def get_subscribers_list(self, max_inter=None):
        subscribers, _ = self.get_sub_subp()
        button_xpath = '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a'

        subscribers_list = self.get_inst_list(button_xpath, max_inter, subscribers)

        return subscribers_list

    def get_subscriptions_list(self, max_inter=None):
        _, subscriptions = self.get_sub_subp()
        button_xpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'

        subscriptions_list = self.get_inst_list(button_xpath, max_inter, subscriptions)

        return subscriptions_list

    def get_inst_list(self, button_xpath, max_inter, cases_num):
        try:
            cases_num = int(cases_num)

        except:
            cases_num = 100

        self.driver.find_element_by_xpath(button_xpath).click() # subscribers or subscriptions button
        time.sleep(2)

        iteration = 1
        while True:
            self.driver.execute_script(f'document.querySelector("body > div.RnEpo.Yx5HN > div > div > div.isgrP").scrollTop={iteration*1000}')
            iteration += 1

            subscribers_list = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div').text

            subscribers_list = subscribers_list.split('Подписаться')
            subscribers_list = [[j for j in i.split('\n') if j] for i in subscribers_list]
            subscribers_list = [i[0] for i in subscribers_list if i]

            if len(subscribers_list) >= cases_num-2:
                break

            if max_inter:
                if iteration >= max_inter:
                    break 

        close_button_xpath = '/html/body/div[4]/div/div/div[1]/div/div[2]/button'
        self.driver.find_element_by_xpath(close_button_xpath).click()

        return subscribers_list

    def close(self):
        if self.is_hide_display:
            self.display.stop()

def compare(a, b):
    similar = 0
    for i in a:
        for j in b:

            if i == j:
                similar += 1 

                print(i)

    return similar/len(a)

def main():

    login = 'login'
    password = 'password'


    parcer = Parcer(login, password, is_hide_display=True)

    parcer.get_inst_page('zuck')

    print(parcer.get_sub_subp())

    sb = parcer.get_subscribers_list(max_inter=30)
    print(sb)

    sp = parcer.get_subscriptions_list(max_inter=30)
    print(sp)

    parcer.close()

if __name__ == "__main__":
    main()
