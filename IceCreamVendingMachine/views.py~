from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from IceCreamVendingMachine.models import IceCream

# Create your views here.

def index(request):
	all_icecreams = IceCream.objects.order_by('-flavor')
	template = loader.get_template('IceCreamVendingMachine/index.html')
	context = RequestContext(request, { 'all_icecreams': all_icecreams,})
	return HttpResponse(template.render(context))

def detail(request, iceCreamID):
    return HttpResponse("You're looking at poll %s." % iceCreamID)

def login(request):
	return render(request, 'IceCreamVendingMachine/index.html')
	
def failureBuy(request):
	return render(request, 'IceCreamVendingMachine/failureBuy.html')

def failureLogin(request):
	return render(request, 'IceCreamVendingMachine/failureLogin.html')

def iceCreamList(request):
	
	return render(request, 'IceCreamVendingMachine/iceCreamList.html')

def receipt(request):
	return render(request, 'IceCreamVendingMachine/receipt.html')
	
def storeAvailableList(request):
	return render(request, 'IceCreamVendingMachine/storeAvailableList.html')

def storeList(request):
	return render(request, 'IceCreamVendingMachine/storeList.html')
	
def successBuy(request):
	return render(request, 'IceCreamVendingMachine/successBuy.html')

def successLogin(request):
	return render(request, 'IceCreamVendingMachine/successLogin.html')


