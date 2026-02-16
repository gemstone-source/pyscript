import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = {'User-Agent': 'Gemstone'}

# def get_url(url,tag):
#     response = requests.get(url,headers=headers)

#     soup = BeautifulSoup(response.content, 'html.parser')
#     tags = soup.find_all(tag)

#     # if tag is not None and tag != "":
#     for tag in tags:
#         urls = tag.get("href")
#         print(urls)

visited_urls = set()

def get_spider(url,tag,keyword):
    try:
        response = requests.get(url,headers=headers)
    except:
        print("Page Not Found:",url)
        sys.exit()

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        tags = soup.find_all(tag)
        
        urls = []
        for tag in tags:
            href = tag.get('href')
            if href is not None and href != "":
                urls.append(href)
        # print(urls)

        for urls2 in urls:
            urls_join = urljoin(url,urls2)
             
            if urls2 not in visited_urls:
                visited_urls.add(urls_join)

                if keyword in urls_join:
                    print(urls_join)
                    get_spider(urls_join, tag, keyword)

if __name__ == "__main__":
    if len(sys.argv) !=4:
        print("Usage: python spider.py <url> <tag> <keyword>")
        sys.exit(1)
    
url = sys.argv[1]
tag = sys.argv[2]
keyword = sys.argv[3]

get_spider(url,tag,keyword)
