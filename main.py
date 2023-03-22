from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.options import Options
import os
import requests
website = input("输入网址")
n = int(input('一共有多少页'))
#site = str(input('输入网址'))
#website = site   #怎么拼接网址 ,第一页无法打印的问题
#website = 'https://www.imn5.net/XiuRen/YouMi/11422.html'
filepath = r'I:\图片'
driverpath = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python311\msedgedriver.exe'
#option = webdriver.EdgeOptions()
options = Options()
options.add_argument("headless")
browser = webdriver.Edge( executable_path= driverpath,options=options)
browser.get(website)

web = website[:-5]





pic_name = browser.find_element(By.CSS_SELECTOR,'body > section > div.imgwebp > p > img:nth-child(1)').get_attribute('alt')#怎么获得元素名字

pic_list =[]
for i in range(n+1):
    url = web + '_' + str(i) + '.html'
    browser.get(url)
    pic_num = browser.find_elements(By.TAG_NAME, 'img')
    for i in range(len(pic_num)):
        b = '/html/body/section/div[2]/p/img[{0}]'.format(i+1)
        element = browser.find_elements(By.XPATH,b)
        for i in range (len(element)):
            element_string = element[i].get_attribute('src')
            pic_list.append(element_string)
            print(element_string)
browser.close()
if not os.path.exists(os.path.join(filepath, pic_name)):
    os.mkdir(os.path.join(filepath,pic_name))

for i in range(len(pic_list)):
    try:
        r = requests.get(pic_list[i])
    except:
        continue
    img_path = os.path.join(os.path.join(filepath,pic_name),f'{i+1}'+'.jpg')
    with open(img_path,mode='wb') as f:
         f.write(r.content)
         f.close()
         print('第{0}张图片保存成功'.format(i+1))

ActionChains(browser).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()

