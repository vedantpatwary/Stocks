from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

def getCookies():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without opening a browser (optional)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection
    chrome_options.add_argument(f"user-data-dir=/Users/vedantpatwary/Library/Application Support/Google/Chrome/Profile 1")  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open Screener login page
    driver.get("https://www.screener.in/login/")

    # Wait for the page to load (increase if needed)
    time.sleep(5)

    # Extract cookies after login
    cookies = driver.get_cookies()

    # Convert cookies to a format usable for requests
    cookies_dict = {cookie["name"]: cookie["value"] for cookie in cookies}

    # Close Selenium browser
    driver.quit()

    # Step 2: Use requests to call Screener API

    # Make the API request using extracted cookies

    return cookies_dict
