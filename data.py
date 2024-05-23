import requests
import pandas as pd
url = 'https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-C0032-005?Authorization=CWA-37DA8724-749A-40D4-9AF4-9F7DD7C3380F&downloadType=WEB&format=JSON'
data = requests.get(url)
data_json = data.json()
location = data_json['cwaopendata']['dataset']['location']
print(list(pd.DataFrame(location)['locationName']))
# for i in location:
#   name = i['locationName']                    # 測站地點
#   city = i['parameter'][0]['parameterValue']  # 城市
#   area = i['parameter'][2]['parameterValue']  # 行政區
#   print(city, area, name)