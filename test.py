# import requests
# import sys
#
# url = "http://10.129.227.148"
#
# def loop():
#     for word in sys.argv[1:]:
#         res =  requests.get(url =f"http://10.129.227.148/{word}")
#         if res.status_code == 404:
#             # print(word)
#             loop()
#         else:
#             data = res.json()
#             print(data)
#             print(res.status_code)
#
# loop()
# from dicto import student_grades
from urllib.parse import urljoin

# from spider import visited_urls

# student_grades = {}
#
# off = False
# while not off:
#     name = input("Enter your name: ")
#     grade  = input("Enter your student_grades: ")
#     student_grades[name] = grade

import requests
from bs4 import BeautifulSoup

visited_urls = set()

def grabber(url,keyword):
    try:
        response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    except:
        print(f"The url {url} was not found.")


    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tag = soup.find_all('link')
        urls = []
        for tag in a_tag:
            urls.append(tag.get('href'))
        # print(urls)

        for urls2 in urls:
            if urls2 not in visited_urls:
                visited_urls.add(urls2)
                url_join = urljoin(url, urls2)

                if keyword in url_join:
                    print(url_join)
                    grabber(url_join,keyword)





url = "https://vodacom.co.tz/fwa"
keyword = "http"

grabber(url,keyword)