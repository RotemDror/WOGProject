import requests
import re
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_scores_service(url):

    try:
        options = webdriver.ChromeOptions()
        web_driver = webdriver.Chrome(options=options)
        web_driver.get(url)
        data = web_driver.find_element(By.XPATH, "/html/body/p")
        data = data.get_attribute('innerHTML')

        if "Your score is:" in data:
            match = re.search(r'Your score is: (\d+)', data)

            if match:
                score = int(match.group(1))
                if 0 <= score <= 1000:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def main_function():

    test = test_scores_service("http://127.0.0.1:8777/")

    if test:
        exit(code=0)
    else:
        exit(code=-1)


main_function()
