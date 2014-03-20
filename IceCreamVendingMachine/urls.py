from django.conf.urls import patterns, url

from IceCreamVendingMachine import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),

	url(r'^(?P<iceCreamID>\d+)/$', views.detail, name='detail'),

	url(r'^/login/$', views.login, name='login'),

	url(r'^/cart/$', views.cart, name='cart'),

)
