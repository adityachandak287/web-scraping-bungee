import requests
import urllib.request
from bs4 import BeautifulSoup
import time
import re
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Accessing URL from .env file
url = os.getenv("PAGE_URL")

if "data" not in os.listdir(os.getcwd()):
    os.mkdir("data")
    print("./data folder created")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
script_tag = soup.find_all('script')[5].text

img_string = re.findall('\[.*?\]', script_tag)
images = json.loads(img_string[0])
print("{} images found".format(len(images)))

img_names = []
for image in images:
    img_url = image["url"]
    img_name = re.findall('IMG_\d{4}.*', img_url)
    if len(img_name) > 0:
        img_names.append(img_name[0])
        if img_name[0] not in os.listdir("data"):
            img_data = requests.get(img_url)
            with open(os.path.join(os.getcwd(), "data", img_name[0]), "wb") as img_file:
                img_file.write(img_data.content)
            # urllib.request.urlretrieve(img_url, os.path.join(os.getcwd(), "data", img_name[0]))
            print(img_name[0] + " saved.")
            time.sleep(1)
        else:
            print(img_name[0] + " skipped.")

print("Completed downloading {} images".format(len(img_names)))
