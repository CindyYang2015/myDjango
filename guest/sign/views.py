from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
	#return HttpResponse("hello kitty")
	return render(request,"index.html")
	
def login_action(request):
	if request.method=='POST':
		username=request.POST.get('username','')
		password=request.POST.get('pwd','')
		if username=='admin' and password=='123':
			return HttpResponseRedirect('/event_manage/')
		else:
			return render(request,'index.html',{'error':'username or password error!'})

def test(request):
	return  HttpResponse('SB')
	
def event_manage(request):
	return render(request,'event_manage.html')