import requests
import re
import webbrowser
import time


"""
Returns the profile picture of the person whose account link is given.
python get_image.py
"""
user_input = input("account link : ")

pattern = "https://i.scdn.co/image/\w*"

response = requests.get(user_input).text

locations = re.search(pattern, response)

try:
    webbrowser.open(response[locations.span()[0] : locations.span()[1]])
except:
    print("link was not found")
    time.sleep(10)


