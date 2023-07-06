import random
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.common.action_chains import ActionChains



# # webdriver設定
# options = Options()
# options.add_argument('--ignore-certificate-errors')
# # options.add_argument('--headless')
# options.add_argument('--ignore-ssl-errors')
# browser = webdriver.Chrome(executable_path = "C:\chromedriver\chromedriver.exe", options=options)
# browser.implicitly_wait(3)
# browser.maximize_window()




def access(mainurl):
    browser.get(mainurl)
    time.sleep(3)
    return mainurl

#ページ内移動
def movepage(mainurl):
    print(mainurl)
    elements = browser.find_elements_by_xpath("//a[contains(@href, '{}')]".format(mainurl))
    print(elements)

    element = random.choice(elements)
    # ActionChains(browser).move_to_element(element).perform()
    print(element)
    urlt = element.get_attribute("href")
    # clicker =element.click()
    # browser.execute_script("arguments[0].click();", element)
    browser.get(urlt)
    time.sleep(3)
    return


def adscraping(classname):
    try:
        print(classname)
        # イメージ取得
        ads = browser.find_elements_by_xpath("//div/*[contains(@id,'imobile')or contains(@class,'article_bodyfooter') or contains(@id,'adunit') or contains(@id,'google-') or contains(@class, 'google') or contains(@class,'adsbox') or contains(@id, 'ad_unit') or contains(@class, 'side-ad') or contains(@id, 'ads') or contains(@class, 'ad0')  or contains(@class, 'admid') or @iframe or contains(. ,'Sponsored') and @data-item-id  ]")
        # ads = browser.find_elements_by_xpath("//*[contains(., 'Sponsored') and @data-item-id]")
        if ads:
            # ランダムなイメージを取得
            # r = random.randint(1, 9)
            # randomimg = browser.find_elements_by_xpath("//img")

            # イメージ保存
            for i, ad in enumerate(ads):

                size = ad.size
                w, h = size['width'], size['height']
                print(i, w, h)
                if w < 51:

                    continue
                elif h < 51:

                    continue
                else:
                    # browser.execute_script("arguments[0].scrollIntoView();", ad)
                    png = ad.screenshot_as_png
                    with open('G:/img/ad{}.png'.format(time.time()), 'wb') as f:
                        f.write(png)
    except InvalidSelectorException:
        print("ERROR!!!")


def ender():
    browser.close()

def quiter():
    browser.quit()

#アクセスするサイトを指定
site = pd.read_csv("../site.csv")
sites = list(site['name'])

def scrapingmachine():
    for i in range(len(sites)):
        acc = sites[i]
        access(acc)
        time.sleep(4)
        for n in range(5):
            adscraping(acc)
            movepage(acc)
            time.sleep(4)


mobile_emulation = {"deviceName": "Pixel 2 XL"}

while True:
    for i in range(5):
        try:
            options = Options()
            options.add_argument('--ignore-certificate-errors')
            # options.add_argument('--headless')
            options.add_argument('--ignore-ssl-errors')
            #スマホモードでスクレイピングするとき用↓
            # options.add_experimental_option("mobileEmulation", mobile_emulation)
            browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe", options=options)
            browser.implicitly_wait(3)
            browser.maximize_window()

            scrapingmachine()
            quiter()
        except :
            quiter()
            break

