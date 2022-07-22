# Gmail cookie stealing research

---------
## Research results
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


Ideas on stuff to research:
 - Use burpsuite to copy the cookies ✅
	- Works even from a different country and different IP
 - What cookies are necessary to read mails❓ 
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
```
🤷🏻‍♂️ = Doesn't matter anymore
✅ = Checked, and succefully worked
❌ = Checks, and is not correct
❓ = Still didn't check or go through
```
---------

## Notes
---------

I used burp on my machine, and surfed to `https://mail.google.com/mail/u/0/#inbox`:

