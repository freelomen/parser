import random
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={useragent.random}')
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--headless")
service = Service('D:\\PythonProjects\\parser\\chromedriver\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)


def get_source_html():
    try:
        driver.get("https://www.wildberries.ru/catalog/0/search.aspx?search=мойка#c137763119")
        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_source_html()


if __name__ == "__main__":
    main()
