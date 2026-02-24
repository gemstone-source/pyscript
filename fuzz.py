import requests
import sys

url = "http://10.129.227.148"

def loop():
    for word in sys.argv[1:]:
        res =  requests.get(url =f"http://10.129.227.148/{word}")
        if res.status_code == 404:
            # print(word)
            loop()
        else:
            data = res.json()
            print(data)
            print(res.status_code)

loop()