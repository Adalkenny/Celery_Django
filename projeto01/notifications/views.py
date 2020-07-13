from django.shortcuts import render

# Create your views here.

def indexView(request):
	context={}
	return render(request, 'notifications/index.html', context)