from buzzfeedScraper import getBuzzfeed
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect

@csrf_exempt


def BuzzfeedSet(request):

	#print(request)
	#print (request.method)
#	print(request.POST['word'])

	if(request.method== "POST"):
		print("In buzzfeed set now")
		json = getBuzzfeed(request.POST['word'])
	#	print ("WOAH'")
	#	print (json)
	return HttpResponse(json)
	#return HttpResponse(json)

@csrf_exempt

def requestSet(request):
#	print ("Checking authentication" )
#	if not request.user.is_authenticated():
	#	return redirect('tempaltes/login.html')
	#else:
	return redirect( "templates/index.html")

