import time
import random
import logging 

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

logging.basicConfig(filename="std.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG)

print('=====================================================================================================')
print('Heyy, you have to login manully on tiktok on FieFox Browser on default profile')
print('=====================================================================================================')
time.sleep(4)

ffOptions = Options()
# Set your profile here 
# https://support.mozilla.org/en-US/kb/profile-manager-create-remove-switch-firefox-profiles


ffProfile_Path= '/Users/YOUR-USER-NAME/Library/Application Support/Firefox/Profiles/XYZ.default-release'
ffProfile = FirefoxProfile(ffProfile_Path)

ffOptions.profile = ffProfile

WAIT_TIME = 30

driver = webdriver.Firefox(options=ffOptions)
try: 
    driver.get("https://www.tiktok.com/foryou")
    driver.maximize_window()

    while True:
        time.sleep(WAIT_TIME)
        
        follows = driver.find_elements(By.XPATH, '//div[contains(@class, "DivTextInfoContainer")]' )
        
       #Code partially works
        logger.info(len(follows))
        for to_follow in follows:
            
            try:
                logger.info(to_follow.text)
                button = None
                button = to_follow.find_element(By.XPATH, '//div[text()="Follow"]' ).click()
                logger.info("FollowButtonClicked")     
                time.sleep(1)
            except Exception as e:
                logger.debug(e)
           
        time.sleep(2)
        logger.info("'for' loop finished")      
        #break #debugging only
   
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        
        
except Exception as e:
    logger.error(e)
  
finally:
    logger.info("quit gracefully")
    #driver.quit()