import MySQLdb
from pprint import pprint
from datetime import date
try:
    # py3
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
except ImportError:
    # py2
    from urllib2 import Request, urlopen
    from urllib import urlencode


def _request(symbol, stat):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
    req = Request(url)
    resp = urlopen(req)
    content = resp.read().decode().strip()
    return content
def history(symbol):
	#symbol = 'GOOG'
	start_date = '2013-01-03'
	end_date = '2014-01-04'
	#pprint(yahooAPI.get_historical_prices('GOOG','2013-01-03','2013-01-08'))
	params = urlencode({
        	's': symbol,
        	'a': int(start_date[5:7]) - 1,
        	'b': int(start_date[8:10]),
        	'c': int(start_date[0:4]),
        	'd': int(end_date[5:7]) - 1,
        	'e': int(end_date[8:10]),
        	'f': int(end_date[0:4]),
        	'g': 'd',
        	'ignore': '.csv',
   	 })

	#symbol = 'GOOG'
	url = 'http://ichart.yahoo.com/table.csv?%s' % params
	req = Request(url)
	resp = urlopen(req)
	content = str(resp.read().decode('utf-8').strip())
	daily_data = content.splitlines()
    #return daliy_data
	hist_dict = dict()
	keys = daily_data[0].split(',')
	a = []
	for day in daily_data[1:]:
		day_data = day.split(',')
		a.append(day_data)
	for i in range (0,len(a)):
		print a[i]
history('GOOG')


