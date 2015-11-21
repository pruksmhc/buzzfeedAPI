from buzzfeedScraper import getBuzzfeed
from django.http import HttpResponse

def buzzfeedSet():
	print ("IT WORKED")
	return HttpResponse("DID IT WORK?")


