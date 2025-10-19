from selenium import webdriver
import time


options= webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/LENOVO/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
time.sleep(60)