import argparse
import json
import re
import time
import urllib.request

parser = argparse.ArgumentParser(description='Download all tiktok videos from a user')
parser.add_argument('-u','--user',
                    help='user to download videos from', required=True)
parser.add_argument('-o','--output',
                    help='name convention of the ouput, for example : `-o video` will name the videos `video_1.mp4, video_2.mp4, ...',
                    default='video')
parser.add_argument('--destination', '-d',
                    default='.',
                    help='destination folder to download videos to')

args = parser.parse_args()

USER = args.user
DESTINATION_FOLDER = args.destination
OUTPUT_NAME = args.output

# 1 - Retrieve the list of urls from the user page
# 2 - Download the videos from the list of urls and store them in the destination folder

# 1 - Retrieve the list of urls from the user page
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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

# 2 - Download the videos from the list of urls and store them in the destination folder

for i in range(len(urls)):
    url = urls[i]
    print(f"{i} : processing url {url}")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=desired_capabilities)
    print("Selenium WebDriver started")

    driver.get(url)
    print(f"Page {url} loaded")

    time.sleep(1)

    logs = driver.get_log("performance")
    with open("network_log.json", "w", encoding="utf-8") as f:
        f.write("[")

        # Iterates every logs and parses it using JSON
        for idx,log in enumerate(logs):
            print(f"Processing log {idx}")
            network_log = json.loads(log["message"])["message"]

            # Checks if the current 'method' key has any
            # Network related value.
            if ("Network.response" in network_log["method"]
                    or "Network.request" in network_log["method"]
                    or "Network.webSocket" in network_log["method"]):
                # Writes the network log to a JSON file by
                # converting the dictionary to a JSON string
                # using json.dumps().
                f.write(json.dumps(network_log) + ",")
        f.write("{}]")

    print("Quitting Selenium WebDriver")
    driver.quit()

    json_file_path = "network_log.json"
    print(f"Opening {json_file_path}")
    with open(json_file_path, "r", encoding="utf-8") as f:
        logs = json.loads(f.read())

    # Iterate the logs
    for idx, log in enumerate(logs):
        # Except block will be accessed if any of the
        # following keys are missing.
        try:
            # URL is present inside the following keys
            print(f"Processing log {idx}")
            if log["params"]["response"]["headers"]["content-type"] == 'video/mp4':
                print(log["params"]["response"]["url"])
                url = log["params"]["response"]["url"]
                print(f"Downloading {url}")
                break

            # Checks if the extension is .png or .jpg
        except Exception as e:
            pass
    urllib.request.urlretrieve(url, f"{DESTINATION_FOLDER}/{OUTPUT_NAME}_{i}.mp4")
    print(f"Downloaded {url}")
    print(f"Saved as {DESTINATION_FOLDER}/{OUTPUT_NAME}_{i}.mp4")