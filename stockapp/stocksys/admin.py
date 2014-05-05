from django.contrib import admin

# Register your models here.from stocksys.models import Stock
from stocksys.models import Stock
from stocksys.models import Customer
from stocksys.models import Favorite,News
from stocksys.models import History
from django.conf import settings
#from django.contrib import admin

# Register your models here.
class FavoriteInline(admin.TabularInline):
	model = Favorite
	extra = 3

class HistoryInline(admin.TabularInline):
	model = History
	extra = 3
	#'classes':'collapse'
class StockAdmin(admin.ModelAdmin):
	fieldsets=[
		('Stock name',{'fields':['stock_name','stock_short']}),
		('Price and prediction',{'fields':['stock_price','stock_volume','short_term','long_term'],'classes':['collapse']}),
		('Date information',{'fields':['upd_date'],'classes':['collapse']}),	
	]
	inlines=[HistoryInline]
	list_display=('stock_name','stock_price','stock_volume','upd_date')
	class Media:
          	js = ('http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js','https://www.dropbox.com/s/tkhhehsajvdq0ki/tbinline.js')

class CustomerAdmin(admin.ModelAdmin):
	fieldsets=[
		('user name',{'fields':['user_name']}),
		('password',{'fields':['passward']}),
		('Email',{'fields':['Email']}),	
		('Create date',{'fields':['create_date']}),	
	]
	inlines = [FavoriteInline]
	list_display = ('user_name','passward','Email','create_date','log_in','was_published_recently')
	list_filter = ['create_date']

class FavoriteAdmin(admin.ModelAdmin):
	list_filter = ['create_date']

class HistoryAdmin(admin.ModelAdmin):
	list_filter=['update_time']
class NewsAdmin(admin.ModelAdmin):
	list_display = ('title','url','create_date')
	list_filter = ['create_date']
admin.site.register(Stock,StockAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Favorite,FavoriteAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(History,HistoryAdmin)

