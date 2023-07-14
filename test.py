import requests

url = 'http://raspberrypi4.local:8080/api/light/on'

x = requests.post(url)

print(x.text)