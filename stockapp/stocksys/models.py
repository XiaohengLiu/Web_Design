from django.db import models

# Create your models here.from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Stock(models.Model):
	stock_name=models.CharField(max_length=100)
	stock_short=models.CharField(max_length=100)
	stock_price=models.FloatField()
	short_term=models.CharField(max_length=100)
	long_term=models.CharField(max_length=100)
	stock_volume=models.IntegerField()
	upd_date=models.DateTimeField('date update')
	def __unicode__(self):
		return self.stock_name

class History(models.Model):
	stock=models.ForeignKey(Stock)
	stock_name=models.CharField(max_length=100)
	stock_short=models.CharField(max_length=100)
	stock_open=models.FloatField()
	stock_close=models.FloatField()
	stock_high=models.FloatField()
	stock_low=models.FloatField()
	stock_volume=models.IntegerField('date update')
	update_time=models.DateTimeField('date time')
	def __unicode__(self):
		return self.stock_name

class Customer(models.Model):
	user_name=models.CharField(max_length=100)
	passward=models.CharField(max_length=100)
	Email=models.CharField(max_length=100)
	log_in=models.BooleanField()
	create_date=models.DateTimeField('date created')
	def __unicode__(self):
		return self.user_name
	def was_published_recently(self):
		return self.create_date>=timezone.now()-datetime.timedelta(days=1)
	was_published_recently.admin_order_field='create_date'
	was_published_recently.boolean = True
	was_published_recently.short_description='Created recently?'

class Favorite(models.Model):
	customer = models.ForeignKey(Customer)
	stock_name=models.CharField(max_length=100)
	stock_short=models.CharField(max_length=100)
	stock_price=models.FloatField()
	short_term=models.CharField(max_length=100)
	long_term=models.CharField(max_length=100)
	create_date=models.DateTimeField('date created')
	def __unicode__(self):
		return self.stock_name
	def was_published_recently(self):
		return self.create_date>=timezone.now()-datetime.timedelta(days=1)
	was_published_recently.admin_order_field='create_date'
	was_published_recently.boolean = True
	was_published_recently.short_description='Created recently?'

class News(models.Model):
	title=models.CharField(max_length=100)
	url=models.CharField(max_length=300)
	create_date=models.DateTimeField('date created')
	def __unicode__(self):
		return self.title
	def was_published_recently(self):
		return self.create_date>=timezone.now()-datetime.timedelta(days=1)
	was_published_recently.admin_order_field='create_date'
	was_published_recently.boolean = True
	was_published_recently.short_description='Created recently?'
