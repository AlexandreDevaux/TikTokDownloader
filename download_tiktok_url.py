import json
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def download_tiktok_url(url, idx, DESTINATION_FOLDER, OUTPUT_NAME):
    print(f"{idx} : processing url {url}")
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
        for i, log in enumerate(logs):
            print(f"Processing log {i}")
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
    for i, log in enumerate(logs):
        # Except block will be accessed if any of the
        # following keys are missing.
        try:
            # URL is present inside the following keys
            print(f"Processing log {i}")
            if log["params"]["response"]["headers"]["content-type"] == 'video/mp4':
                print(log["params"]["response"]["url"])
                url = log["params"]["response"]["url"]
                print(f"Downloading {url}")
                break

            # Checks if the extension is .png or .jpg
        except Exception as e:
            pass
    urllib.request.urlretrieve(url, f"{DESTINATION_FOLDER}/{OUTPUT_NAME}_{idx}.mp4")
    print(f"Downloaded {url}")
    print(f"Saved as {DESTINATION_FOLDER}/{OUTPUT_NAME}_{idx}.mp4")