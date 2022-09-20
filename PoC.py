# This is the exact script from the README
import requests

# If you want to see all the emails you can go to this URL
# https://mail.google.com/mail/u/0/#all/pX and X is a page number, i.e https://mail.google.com/mail/u/0/#all/p5
# URL = "https://mail.google.com/mail/u/0/#all/p2"
URL = "https://mail.google.com/mail/u/0/#inbox"
cookies = {
    "SID": "XXXX",
    "OSID": "XXXX",
    "HSID": "XXXX",
    "SSID": "XXXX"
}

def main():
    res = requests.get(URL, cookies=cookies)
    
    # You can use BeautifulSoup to parse the request and look at all the emails and their contents
    print(res.text)

if __name__ == '__main__':
    main()
