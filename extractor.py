import time
import os
from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.common.keys import Keys  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
current_directory = os.getcwd()


options = webdriver.ChromeOptions()
prefs = {"download.default_directory": current_directory}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)


def extractor():

    # Navigate to the login page
    login_url = 'https://secure.bidsandtenders.ca/Module/Tenders/en/Login'

    driver.get(login_url)

    # Enter username and password
    username_field = driver.find_element(By.NAME, 'Username')
    password_field = driver.find_element(By.NAME, 'Password')

    username_field.send_keys('smlngsh@gmail.com')
    password_field.send_keys('SAM.abri@aze1')

    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'btn-success'))
        )
        # Submit the form
        login_button.click()
    except TimeoutException:  # type: ignore
        print("Login button not found or page took too long to load.")
        driver.quit()
        exit()
    bid_url = 'https://burlington.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c648d968-5777-4d9f-9ac1-74dc1213a63d'
    driver.get(bid_url)
    # Wait for the dashboard page to load

    # download the Html
    html_content = driver.page_source

    # Parse the HTML content with BeautifulSoup

    # for tag in body_content.find_all():
    #     if tag.string:
    #         words = tag.string.split()
    #         if len(words) < 10:
    #             tag.decompose()
    #     else:
    #         text = tag.get_text(" ", strip=True)
    #         words = text.split()
    #         if len(words) < 10:
    #             tag.decompose()

    # body_str = str(body_content).replace('\u00a0', ' ')

    with open("tender.html", "w", encoding="utf-8") as file:
        file.write(str(html_content))

    # download pdf
    driver.find_element(By.ID, 'ext-gen113').click()
    try:
        download_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'ext-gen113'))
        )
        # Submit the form
        download_button.click()
    except TimeoutException:  # type: ignore
        print("Login button not found or page took too long to load.")
        driver.quit()
        exit()
    # Perform actions as needed...
    time.sleep(30)
    # Close the driver
    driver.quit()


extractor()
