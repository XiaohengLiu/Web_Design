from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from stocksys.models import Stock,Customer,Favorite,News,History
from django.http import HttpResponse
from yahooAPI import get_price,get_volume
from django.utils import timezone
from shortTerm import shortTerm
from LongTerm import longTerm
from django.template import Context,loader
import datetime as dt
import pandas.io.data as web

def index(request):
	return render_to_response('stock/index.html')
def index1(request):
	return render_to_response('stock/index1.html')

def search(request):
	stockName = request.GET['stockName']
	if stockName=='':
		message='You submittend an empty form'
		return render_to_response('stock/index1.html',{'message':message})
	else: #'stockName' in request.GET:
		#stockName = request.GET['stockName']
		stocks=Stock.objects.filter(stock_name__icontains=stockName)
		for st in stocks:
			st.stock_price=get_price(st.stock_short)
			st.save()
			st.upd_date=timezone.now()
			st.save()
			st.stock_volume=get_volume(st.stock_short)
			st.save()
			st.short_term=shortTerm(st.stock_short)
			st.save()
			st.long_term=shortTerm(st.stock_short)
			st.save()
		#stocks.save()
		
		return render_to_response('stock/search_result.html',{'stocks':stocks,'query':stockName})
	"""else:
		message='You submittend an empty form'
		return HttpResponse(message)"""

def register(request):
	return render_to_response('stock/register.html')

def reglogin(request):
	check=''
	errormessage=''
	name=''
	username=request.GET.get('userName')
	usn=Customer.objects.filter(user_name=username)
	for us in usn:
		name=us.user_name
	psswd=request.GET.get('password')
	rpsswd=request.GET.get('rpsswd')
	eml=request.GET.get('email')
	if psswd != rpsswd:
		errormessage='password dose not match'
	elif username==name:
		errormessage='user name has been registed'
	else:
		c=Customer(user_name=username,passward=psswd,Email=eml,log_in=False,create_date=timezone.now())
		c.save()
		check='True'
	return render_to_response('stock/reglogin.html',{'check':check,'errormessage':errormessage})


def login(request):
	return render_to_response('stock/login.html')


def lindex(request):
	name=''
	psd=''
	errormessage=''
	message=''
	check=False
	username=request.GET.get('userName')
	usn=Customer.objects.filter(user_name=username)
	for us in usn:
		name=us.user_name
		#sid=us.id
		message = " %s "%name
		psd=us.passward
	psswd=request.GET.get('password')
	if name=='':
		errormessage='Wrong user name'
	elif psd!=psswd:
		errormessage='Wrong password'
	else:
		for check in usn:
			check.log_in = True
			check.save()
	return render_to_response('stock/lindex.html',{'check':check,'errormessage':errormessage,'message':message,'usn':usn})

def logout(request,customer_id):
	usr=Customer.objects.filter(pk=customer_id)
	for user in usr:
		user.log_in=False
		user.save()	
	return render_to_response('stock/logout.html')

def favorite(request,customer_id):
	usr=get_object_or_404(Customer,pk=customer_id)
	usn=Customer.objects.filter(pk=customer_id)
	f=Favorite.objects.filter(customer_id=customer_id)
	for favor in f:
		stocks=Stock.objects.filter(stock_name=favor.stock_name)
		for st in stocks:
			st.stock_price=get_price(st.stock_short)
			st.save()
			st.stock_volume=get_volume(st.stock_short)
			st.save()
			st.upd_date=timezone.now()
			st.save()
			st.short_term=shortTerm(st.stock_short)
			st.save()
			st.long_term=shortTerm(st.stock_short)
			st.save()
			favor.stock_price=st.stock_price
			favor.save()
			favor.stock_short=st.stock_short
			favor.save()
			favor.create_date=st.upd_date
			favor.save()
			favor.short_term=st.short_term
			favor.save()
			favor.long_term=st.long_term
		 	favor.save()
	return render_to_response('stock/favorite.html',{'usr':usr,'usn':usn})
		
				
def add(request,customer_id):
	sname=request.GET.get('sname')
	usr=get_object_or_404(Customer,pk=customer_id)
	a=customer_id
	usr.favorite_set.create(stock_name=sname,stock_price=0,stock_short='null',short_term='null',long_term='null',create_date=timezone.now())
	return render_to_response('stock/add.html',{'usn':a})

def delete(request,customer_id):
	sname=request.GET.get('sname')
	usr=get_object_or_404(Customer,pk=customer_id)
	a=customer_id
	d = usr.favorite_set.filter(stock_name=sname)
	d.delete()
	return render_to_response('stock/delete.html',{'usn':a})

def news(request):
	nw=News.objects.all()
	return render_to_response('stock/news.html',{'news':nw})

def update(request):
	start = dt.datetime.now()-dt.timedelta(days=30)
	end = dt.datetime.now()
	a=['MSFT','GOOG','AMZN','YHOO','AAPL']
	for shrt in a:
		stk=get_object_or_404(Stock,stock_short=shrt)
		data = web.get_data_yahoo(shrt,start,end)
		stk.stock_price=get_price(stk.stock_short)
		stk.save()
		stk.upd_date=timezone.now()
		stk.save()
		stk.stock_volume=get_volume(stk.stock_short)
		stk.save()
		stk.short_term=shortTerm(stk.stock_short)
		stk.save()
		stk.long_term=shortTerm(stk.stock_short)
		stk.save()
		a = dt.datetime.now()
		for i in range(0,len(data.Open)):
			if a.isoweekday>5:
				a-=dt.timedelta(days=2)
			stk.history_set.create(stock_name=stk.stock_name,stock_short=stk.stock_short,stock_open=data.Open[i],stock_volume=data.Volume[i],stock_close=data.Close[i],stock_high=data.High[i],stock_low=data.Low[i],update_time=a)
		a -= dt.timedelta(days=1)
		
	return render_to_response('stock/update.html')

def history(request):
	import random
	import django
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    	from matplotlib.figure import Figure
    	from matplotlib.dates import DateFormatter
	
	stockName = request.GET['stName']
	#stock=get_object_or_404(Stock,stock_name=stockName)
	start = dt.datetime.now()-dt.timedelta(days=20)
	end = dt.datetime.now()
	data = web.get_data_yahoo(stockName,start,end)
   	fig=Figure()
    	ax=fig.add_subplot(111)
    	x=[]
    	y=[]
	
    	now=dt.datetime.now()
    	delta=dt.timedelta(days=1)
    	for i in range(10):
        	x.append(now)
        	now-=delta
		a=data.Close[i]
        	y.append(a)
    	ax.plot_date(x, y, '-')
    	#ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    	fig.autofmt_xdate()
    	canvas=FigureCanvas(fig)
    	response=django.http.HttpResponse(content_type='image/png')
    	canvas.print_png(response)
	t=loader.get_template('stock/history.html')
    	return response

def query(request):
	start = dt.datetime.now()-dt.timedelta(days=10)
	end = dt.datetime.now()
	data = web.get_data_yahoo('GOOG',start,end)
	max_google=max(data.Close)
	start = dt.datetime.now()-dt.timedelta(days=365)
	end = dt.datetime.now()
	data1 = web.get_data_yahoo('MSFT',start,end)
	avg1 = sum(data1.Close)/len(data1.Close)
	m1=min(data1.Close)
	data5 = web.get_data_yahoo('GOOG',start,end)
	m2=min(data5.Close)
	avg2 = sum(data5.Close)/len(data5.Close)
	data2 = web.get_data_yahoo('AAPL',start,end)
	m3=min(data2.Close)
	avg3 = sum(data2.Close)/len(data2.Close)
	data3 = web.get_data_yahoo('AMZN',start,end)
	m4=min(data3.Close)
	avg4 = sum(data3.Close)/len(data3.Close)
	data4 = web.get_data_yahoo('YHOO',start,end)
	m5=min(data4.Close)
	avg5 = sum(data4.Close)/len(data4.Close)
	
	idfinder=[]
	if avg1<m2:
		idfinder.append('MSFT')
	if avg3<m2:
		idfinder.append('AAPL')
	if avg4<m2:
		idfinder.append('AMZN')
	if avg5<m2:
		idfinder.append('YHOO')
	ids=[]
	for sht in idfinder:
		stock = get_object_or_404(Stock,stock_short=sht)
		ids.append(stock.id)
	
	return render_to_response('stock/query.html',{'hprice_google':max_google,'avg_m':avg1,'l_m':m1,'l_g':m2,'l_a':m3,'l_mz':m4,'l_yh':m5,'ids':ids})
	















