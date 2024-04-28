import requests
import time
from datetime import datetime

cookie = ""
parameters = ""
username = ""
link = ""
tpt = 0
times = 0


def main():
    get_cookie_and_parameters()
    input("Press Enter to exit")


def complete_request():
    global cookie, parameters, username, link, tpt, times

    headers = {
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "origin": "https://www.textivate.com",
        "referer": "https://www.textivate.com/m_million.php?ul=2",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    }
    
    print("Generating Parameters!")
    current_time_seconds = int(time.time())
    a = round(current_time_seconds)
    b = convert_to_base36(tpt + a)
    c = reverse_string(b)
    print("Generating htpt!")
    print("htpt:", c)
    print("Forming correct parameters!")

    data = {
        "challid": link[36:],
        "stname": username,
        "stgroup": "",
        "score": tpt,
        "stamp": str(current_time_seconds),
        "activityfb": tpt,
        "htpt": c,
        "indstudname": "",
        "pwn": 0,
    }

    print("PARAMETERS:", data)

    good = True

    for i in range(times):
        if good:
            print("Sending request...")
        else:
            pass

        response = requests.post("https://www.textivate.com/challengepoints.php", data=data, headers=headers)
        res = response.text
        if good:
            print("Request sent successfully!")
            print(res)
            good = False
        else:
            good = True

        time.sleep(0.1)


def reverse_string(s):
    return s[::-1]


def convert_to_base36(number):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    result = ""

    while number > 0:
        remainder = number % 36
        result = chars[remainder] + result
        number //= 36

    return result


def get_cookie_and_parameters():
    global link, username, tpt, times
    print("CREATED BY IHAVEGOODNAME.")
    link = input("Enter textivate link: ")
    username = input("Enter username: ")
    tpt = int(input("Enter score: "))
    times = int(input("Enter amount of times to loop: "))

    print("\nComplete Request:")
    complete_request()


if __name__ == "__main__":
    main()
