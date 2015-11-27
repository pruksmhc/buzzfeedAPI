from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from buzzfeed.models import BuzzfeedSearch
from buzzfeed.serializers import BuzzfeedSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


    
    def buzzfeed_list(request):
	    """
	    List all code snippets, or create a new snippet.
	    """
	    if request.method == 'GET':
	    	#get all teh buzzfeed stuff. 
	        snippets = BuzzfeedSearch.objects.all()
	        serializer = BuzzfeedSerializer(snippets, many=True)
	        return JSONResponse(serializer.data)

	    elif request.method == 'POST':
	        data = JSONParser().parse(request)
	        serializer = BuzzfeedSerializer(data=data)
	        if serializer.is_valid():
	            serializer.save()
	            return JSONResponse(serializer.data, status=201)
	        return JSONResponse(serializer.errors, status=400)