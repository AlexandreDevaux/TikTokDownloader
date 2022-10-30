import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def getUrlsFromUserName(USER, DESTINATION_FOLDER):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    print("Selenium WebDriver started")


    driver.get(f'https://www.tiktok.com/@{USER}')
    print(f"Page https://www.tiktok.com/@{USER} loaded")

    # wait for the page to load
    time.sleep(1)

    SCROLL_PAUSE_TIME = 2

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    counter = 0
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(f"Scrolling down for the {counter} time")
        counter += 1

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    print("Scrolling down finished")


    # get html of the page
    html = driver.page_source
    print("HTML retrieved")
    driver.quit()
    print("Selenium WebDriver stopped")

    print("Parsing HTML")
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
    urls = list(filter(lambda x :f"@{USER}/video/" in x, urls))
    print(f"{len(urls)} urls found")

    # write urls to a file in destination folder
    with open(f"{DESTINATION_FOLDER}/urls.txt", "w") as f:
        f.write('\r'.join(urls))
    print(urls[:10])
    return urls