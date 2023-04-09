from selenium import webdriver
import numpy as np
import cv2
import pyautogui
import time
from Detection import data



driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/index.htm")



def test():
 count = 0
 Url = ''
 l = '' # last visited url
 if driver.current_url == data.test_url:
        print("Same Page")
 else :
       
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        if(Url != driver.current_url ):
  
           if(l != driver.current_url):
            if(data.sc_taken<=3):
             data.sc_url[data.sc_taken] = 'ResultAssets/Browser_switch/frame' + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"
             cv2.imwrite( 'ResultAssets/Browser_switch/frame' + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg",image)
             data.sc_taken = data.sc_taken + 1

           l = driver.current_url
          
           data.switch = data.switch + 1
           data.tabswitch = True
           data.URL.add(driver.current_url)
        Url = driver.current_url
        count = count + 1
        print("Different Page")   
