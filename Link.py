import requests
import json
print('Link vertise Bypasser')
link = input ('Put Link Here:')
response = requests.get("https://bypass.bot.nu/bypass2?url=" + link)
destination = response.json()['destination']
print(destination)