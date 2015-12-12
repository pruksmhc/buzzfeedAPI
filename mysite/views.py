from buzzfeedScraper import getBuzzfeed
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect
from django.template import loader, Context
from buzzfeed.models import BuzzfeedSearch
from buzzfeed.serializers import BuzzfeedSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.template import RequestContext
import json
import urllib



@csrf_exempt


def BuzzfeedSet(request):

	#print(request)
	#print (request.method)
#	print(request.POST['word'])

	if(request.method== "POST"):
	#	print("In buzzfeed set now")
		json = getBuzzfeed(request.POST['word'])
	#	print ("WOAH'")
	#	print (json)
	return HttpResponse(json)
	#return HttpResponse(json)

@csrf_exempt

def history(request):
    template = loader.get_template('history.html')
    query_results = BuzzfeedSearch.objects.order_by('created')
   # print(query_results)
   # print(type(query_results))
   # print("YO")
    for query in query_results:
    	data = query.json
        jsonList = []
        jsonList.append(json.dumps(data))
        jsonStr = "text/json;charset=utf-8," +  urllib.quote(data) 
        query.json = jsonStr

    context = RequestContext(request, {
        'query_results': query_results.reverse(),
    })

    return HttpResponse(template.render(context))

@csrf_exempt

def requestSet(request):
#	print ("Checking authentication" )
#	if not request.user.is_authenticated():
	#	return redirect('tempaltes/login.html')
	#else:
	return redirect( "templates/index.html")

