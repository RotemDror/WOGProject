import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def test_scores_service(url):

    try:
        options = webdriver.ChromeOptions()
        web_driver = webdriver.Chrome(service=Service("./chromedriver"),options=options)
        web_driver.get(url)
        WebDriverWait(web_driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/p")))
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
