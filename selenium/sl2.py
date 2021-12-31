import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
mydriver = webdriver.Chrome()
address = 'https://api.snappfood.ir/restaurant/menu/p5wjme/shila/shariati'
class infinite_scroll(object):
  def __init__(self, last): 
    self.last = last
  def __call__(self, driver):
    new = driver.execute_script('return document.body.scrollHeight')  
    if new > self.last:
        return new
    else:
        return False
def scroll_until_end(mydriver):
    last_height = mydriver.execute_script('return document.body.scrollHeight')
    flag=1
    while flag==1:
        mydriver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        try:
            wait = WebDriverWait(mydriver, 10)
            new_height = wait.until(infinite_scroll(last_height))
            last_height = new_height
        except:
            print("End of page reached")
            flag = 0
def parse(driver,address,SCROLL_PAUSE_TIME = 0.5):
    driver.get(address)
    scroll_until_end(driver)
    A = driver.find_elements(By.CSS_SELECTOR,"div.kk-grid-item")
    print(len(A))
    #for it in A:
    #    image = it.find_elements(By.TAG_NAME,"img")
    #    img_src = image[0].get_attribute("src")
    #    print(img_src)
    for it in A:
        print("item")
        container = it.find_elements(By.CSS_SELECTOR,'div.kk-has-image')
        if len(A) > 0:
            image = container[0].find_elements(By.TAG_NAME,"img")
            img_src = image[0].get_attribute("src")
            print(img_src)
    print("OHHH")