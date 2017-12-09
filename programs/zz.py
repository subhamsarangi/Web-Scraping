import requests
import json
from bs4 import BeautifulSoup

url='https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json'

response = requests.get(url)

response_dict = response.json()
time, data = response_dict['time'], response_dict['data']
serialized_data = json.dumps(data)
print(serialized_data)
print(time)