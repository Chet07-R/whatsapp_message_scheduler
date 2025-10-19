from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


options=webdriver.ChromeOptions()
# to save user's profile
# otherwise we'll have to log-in to whatsapp each time we run this script
options.add_argument("user-data-dir=C:/Users/LENOVO/Desktop/chetan/AutomationProfile")
driver=webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,100)

# as the target is inside span tag(we are targetting XPath here)
# target='"Sparsh"'

target='Sparsh'
message='testing'

search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
search_box = wait.until(EC.presence_of_element_located((By.XPATH, search_xpath)))

print(f"Searching for {target}...")

# Clear previous search
search_box.clear()
time.sleep(1)
search_box.send_keys(target)
time.sleep(2)
search_box.send_keys(Keys.ENTER)
time.sleep(3)


# Whatsapp uses a thing called lazy loading so i there was a problem in sending messages to older contact so we are using the above code snippet to directly search contact

# general syntax of xpath- XPath=//tagname[@attribute='value']
# try:
#     contact_path = f'//span[@title={target}]'
#     contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_path)))
# except:
#     contact_path = f'//span[contains(@title,{target})]'
#     contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_path)))
# contact.click()


message_box_path='//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div[1]/p'
message_box=wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
message_box.send_keys(message + Keys.ENTER)

print("Message sent. Press Enter to close the browser...")
input() 


driver.quit()