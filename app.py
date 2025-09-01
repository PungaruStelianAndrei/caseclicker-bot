from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from keep_alive import keep_alive
import os

keep_alive()  # pornește endpoint-ul pingabil

USERNAME = "andrei04pungaru@gmail.com"
PASSWORD = ")$pungaru04"
URL = "https://case-clicker.com/"

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# pe Replit trebuie să folosim chromedriver instalat în environment
driver = webdriver.Chrome(options=options)

try:
    driver.get(URL)
    time.sleep(5)

    # TODO: Click login și completare user/pass
    print("Am deschis site-ul și sunt logat (simulat)!")

    while True:
        time.sleep(60)

finally:
    driver.quit()
