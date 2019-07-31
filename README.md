# Web Scraping using Python
Script to scrape face adrenalin website and download all relevant images.

![python-3.7.3](https://img.shields.io/badge/python-3.7.3-blue)
![pip-19.2.1](https://img.shields.io/badge/pip-19.2.1-brightgreen)

## Setup
### Requirements
Use the package manager *pip* to install required libraries from "requirements.txt":

```cmd
pip install -r requirements.txt
```
___
### URL
Create *.env* file to store page URL (example given in *.sample_env*):
```
PAGE_URL="YOUR_URL_HERE"
```
**_OR_**

Edit following line in code and assign page URL to `url` variable:
```python
url = os.getenv("PAGE_URL")
#Change above line to look something like the line below
url = "YOUR_URL_HERE"
```
---
Script will make `./data` directory if it doesn't already exist and download images to it.
## Usage
Run script using following command:
```cmd
python scrape.py
```
Images that are already downloaded will be skipped.
