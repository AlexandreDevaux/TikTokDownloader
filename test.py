import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
print("Selenium WebDriver started")

# load cookies from json file to selenium
import json

with open('cookie.json', 'r', encoding='utf-8') as f:
    cookies = json.load(f)

driver.get(f'https://www.tiktok.com/')


for cookie in cookies:
    driver.add_cookie(cookie_dict=cookie)

# refresh the page
driver.refresh()



# wait for the page to load
time.sleep(99)