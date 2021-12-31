import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
mydriver = webdriver.Chrome()
address = 'https://api.snappfood.ir/restaurant/menu/p5wjme/shila/shariati'
mydriver.get(address)
class infinite_scroll(object):
  def __init__(self, last): 
    self.last = last
  def __call__(self, driver):
    new = driver.execute_script('return document.body.scrollHeight')  
    if new > self.last:
        return new
    else:
        return False


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




address = 'https://api.snappfood.ir/restaurant/menu/p5wjme/shila/shariati'
def infinite_scroll(driver):
    last_height = driver.execute_script('return document.body.scrollHeight')
flag=1
while flag==1:

  driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

  try:
   wait = WebDriverWait(driver, 10)

   new_height = wait.until(infinite_scroll(last_height))
   last_height = new_height

  except:
      print("End of page reached")
      flag = 0


def parse(address,SCROLL_PAUSE_TIME = 0.5):
    driver.get(address)
    pass
#driver.get("http://www.google.com")
#print(driver.page_source.encode('utf-8')) 
#a = driver.find_elements(By.XPATH,'//*[@id="kkgridpos-8484478"]/div[1]/img') kk-image-container kk-has-image
#src = a[0].get_attribute('src')
#a = driver.find_elements(By.XPATH,'//*[@id="kkgridpos-8484478"]/div[1]/img')

# Get scroll height

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(new_height)
    if new_height - last_height < 50:
        break
    last_height = new_height

A = driver.find_elements(By.CSS_SELECTOR,"div.kk-grid-item")

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



