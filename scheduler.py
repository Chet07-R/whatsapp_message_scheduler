from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

data = pd.read_excel("contacts.xlsx")

options=webdriver.ChromeOptions()
# to save user's profile
# otherwise we'll have to log-in to whatsapp each time we run this script
options.add_argument("user-data-dir=C:/Users/LENOVO/Desktop/chetan/AutomationProfile")
driver=webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,100)

# as the target is inside span tag(we are targetting XPath here)
# target='"Sparsh"'


search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
wait.until(EC.presence_of_element_located((By.XPATH, search_xpath)))


for index, row in data.iterrows():
    name = row['Name']
    message = row['Message']
    image_path = row['ImagePath']


    search_box = wait.until(EC.presence_of_element_located((By.XPATH, search_xpath)))
    search_box.clear()
    time.sleep(1)
    search_box.send_keys(name)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)

    #image
    attach_xpath = '//span[@data-icon="clip"]'
    attach_button = wait.until(EC.presence_of_element_located((By.XPATH, attach_xpath)))
    attach_button.click()
    time.sleep(1)

    image_upload_xpath = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'
    image_box = wait.until(EC.presence_of_element_located((By.XPATH, image_upload_xpath)))
    image_box.send_keys(image_path)
    time.sleep(3)

    #caption message
    caption_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
    caption_box = wait.until(EC.presence_of_element_located((By.XPATH, caption_xpath)))
    caption_box.send_keys(message)
    caption_box.send_keys(Keys.ENTER)
    time.sleep(3)

    print(f"Message with image sent to {name}")


# Whatsapp uses a thing called lazy loading so i there was a problem in sending messages to older contact so we are using the above code snippet to directly search contact

# general syntax of xpath- XPath=//tagname[@attribute='value']
# try:
#     contact_path = f'//span[@title={target}]'
#     contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_path)))
# except:
#     contact_path = f'//span[contains(@title,{target})]'
#     contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_path)))
# contact.click()



print("All messages sent successfully!")
input("Press Enter to close...")
driver.quit()