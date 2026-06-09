import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://github.com/usernam121"
driver = webdriver.Chrome()
driver.get(url)
repo = "https://github.com/usernam121"

# time.sleep(2)
response = driver.find_elements(By.CLASS_NAME,"repo")
# time.sleep(2)

links = []
flinks = []

def going_for_raw(third_page):
    driver.get(third_page)
    raw = driver.find_element(By.CLASS_NAME,"prc-Button-ButtonBase-9n-Xk")
    raw.click()
    html = driver.page_source
    html = f"{html}"

    if "lorem" in html:
        print("Password found in {third_page}")

def loop(next_page):
    global a
    driver.get(next_page)
    response2 = driver.find_elements(By.CLASS_NAME,"react-directory-truncate")

    for a in response2:
        pass
    if "py" in a.text:
        second_link = f"{next_page}/blob/main/{a.text}"
        # print(second_link)
        going_for_raw(second_link)


for i in response:
    links.append(i.text)
# print(links)

for l in links:
    next_page = f"{repo}/{l}"
    flinks.append(next_page)
    loop(next_page)
# print(flinks)

driver.quit()