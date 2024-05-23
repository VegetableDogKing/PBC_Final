import requests
import pandas as pd
url = 'https://www.cwa.gov.tw/V8/C/W/week.html'
data = requests.get(url)
data_html = data.json()