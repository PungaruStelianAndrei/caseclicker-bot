from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ------------------------------
# CONFIG
USERNAME = "andrei04pungaru@gmail.com"
PASSWORD = ")$pungaru04"
URL = "https://case-clicker.com/"
# ------------------------------

options = Options()
options.add_argument("--headless")  # rulează fără interfață grafică
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get(URL)
    time.sleep(5)  # așteaptă încărcarea site-ului

    # TODO: aici trebuie să dai click pe butonul de login și să completezi câmpurile
    # Exemplu (trebuie adaptat după ce inspectăm site-ul):
    # login_button = driver.find_element(By.LINK_TEXT, "Login")
    # login_button.click()
    # time.sleep(2)
    # username_input = driver.find_element(By.NAME, "username")
    # password_input = driver.find_element(By.NAME, "password")
    # username_input.send_keys(USERNAME)
    # password_input.send_keys(PASSWORD)
    # password_input.send_keys(Keys.RETURN)

    print("Am deschis site-ul și sunt logat (simulat)!")
    while True:
        time.sleep(60)  # ține sesiunea activă

finally:
    driver.quit()
