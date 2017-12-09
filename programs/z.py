import requests
from bs4 import BeautifulSoup

url='https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,'html.parser')

table = soup.find('table',{'id':'topGainers'})
tickers = []
for row in table.findAll('tr')[1:]:
	ticker = row.findAll('td')[0].text
	tickers.append(ticker)
print(tickers)