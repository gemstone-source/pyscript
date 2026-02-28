import time

from selenium import webdriver
from selenium.webdriver.common.by import By





# on = True
# while on:
#     def checking_price():
#         time.sleep(10)
#         driver = webdriver.Chrome()
#         driver.get(url)
#         price = driver.find_element(By.CLASS_NAME,"amount")
#         print(price.text)
#         driver.quit()
#     checking_price()


url = "https://github.com/usernam121"
driver = webdriver.Chrome()
driver.get(url)
res = driver.find_element(By.CLASS_NAME, "repo")
# print(repos.text)



links = []
flink = []

for i in res:
    links.append(i.text)
print(links)

for l in links:
    next_page = f"{url}/{l}"
    flink.append(next_page)
print(flink)
driver.quit()