from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    	# Examples:
    	# url(r'^$', 'stockapp.views.home', name='home'),
    	# url(r'^blog/', include('blog.urls')),
	(r'^images/(?P<path>.*)$','django.views.static.serve',{'document_root':'/home/niboyu/web/templates/stock'+'/images'}),
	(r'^js/(?P<path>.*)$','django.views.static.serve',{'document_root':'/home/niboyu/web/templates/stock'+'/js'}),
	(r'^css/(?P<path>.*)$','django.views.static.serve',{'document_root':'/home/niboyu/web/templates/stock'+'/css'}), 
	#(r'^/history.png$', 'stocksys.views.history'),
	url(r'^histoychr/$', 'stocksys.views.history'),
	url(r'^query/$','stocksys.views.query'),
	url(r'^index/$','stocksys.views.index'),
	url(r'^index/index1.html/$','stocksys.views.index1'),
	url(r'^register/$','stocksys.views.register'),
	url(r'^reglogin/$','stocksys.views.reglogin'),
	url(r'^login/$','stocksys.views.login'),
	url(r'^lindex/$','stocksys.views.lindex'),
	url(r'^logout/(?P<customer_id>\d+)/$','stocksys.views.logout'),
	url(r'^favorite/(?P<customer_id>\d+)/$','stocksys.views.favorite'),
	url(r'^result/$','stocksys.views.search'),
	url(r'^news/$','stocksys.views.news'),
	url(r'^add/(?P<customer_id>\d+)/$','stocksys.views.add'),
	url(r'^update/$','stocksys.views.update'),
	url(r'^delete/(?P<customer_id>\d+)/$','stocksys.views.delete'),
	#url(r'^search/(?P<stock_id>\d+)/$','stocksys.views.detail'),
  	url(r'^admin/', include(admin.site.urls)),
)
