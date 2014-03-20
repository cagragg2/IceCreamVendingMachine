from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from IceCreamVendingMachine.models import IceCream

# Create your views here.

def index(request):
	all_icecreams = IceCream.objects.order_by('-flavor')
	template = loader.get_template('IceCreamVendingMachine/index.html')
	context = RequestContext(request, { 'all_icecreams': 			all_icecreams,})
	return HttpResponse(template.render(context))

def detail(request, iceCreamID):
    return HttpResponse("You're looking at poll %s." % iceCreamID)

def login(request):
	return render_to_response('IceCreamVendingMachine/Login.html')

def cart(request):
	return render_to_response('IceCreamVendingMachine/Cart.html')
	
