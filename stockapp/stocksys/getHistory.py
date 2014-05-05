import math
import numpy as np
import pandas.io.data as web
import datetime
for i in range(0,30):
	a=datetime.datetime.now()-datetime.timedelta(days=i)
	if a.isoweekday()<=5:
		print a
