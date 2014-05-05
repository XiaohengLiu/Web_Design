import matplotlib.pyplot as plt
import math
import numpy as np
import pandas.io.data as web
import datetime

order=5
alpha = 0.005
beta = 11.1

def phy(x):      
	ex = 0
	a = []
	for ex in range (0,order+1):
		a.append(x**ex)
	a = np.array(a)

	return a



def inversion(xa):
	b = np.zeros([order+1,order+1])
	i = np.ones((order+1,order+1))
	j = 0
	for j in range (0,len(xa)):
		fy = phy(xa[j])
		c = order+1
		fy.shape=(c,1)
		tansphy = np.transpose(fy)
		b += np.dot(fy,tansphy)
		
	sm = alpha*i+beta*b
	sm = np.linalg.inv(sm)
	return sm

def mx(x,xa,ya):					#calculating mean
	fy = phy(x)

	c = order+1
	fy.shape=(c,1)
	tansphy = np.transpose(fy)

	sm = inversion(xa)

	m = np.dot(tansphy,sm)
	m = beta*m
	i=0
	sp = np.zeros(order+1)
	for i in range (0,len(xa)):
		py = phy(xa[i])
		tp = py * ya[i]

		sp = np.add(sp,tp)

	m = np.dot(m,sp)
	return m

def s2 (x,xa):						#calculating variance
	fy = phy(x)
	c = order+1
	fy.shape=(c,1)
	tansphy = np.transpose(fy)
	sm = inversion(xa)
	m = np.dot(tansphy,sm)
	m = np.dot(m,fy)
	v = 1/beta + m
	return v

def shortTerm(symbol):
	a=web.get_data_yahoo(symbol, (datetime.datetime.now() - datetime.timedelta(days = 20)), datetime.datetime.now())['Adj Close']
# here are the given number of M, alpha, and beta
	

	xa=[]
	for i in range(0,len(a)):
		xa.append(i)
	ya=a
	plt.figure(1)
	value = 11
	ss = s2 (value,xa)
	mm = mx(value,xa,ya)
	s = ss[0][0]
	m = mm[0]							#print the mean and variance
	#print m

	index = m - ya[len(a)-1]
	if(index < -m*0.005):
        	return "Sell"
	elif(index < m*0.005):
        	return "Hold"
	else:
        	return "Buy More"


shortTerm('AAPL')	
					#plot the probability density fun


