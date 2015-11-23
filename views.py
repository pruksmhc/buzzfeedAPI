from buzzfeedScraper import getBuzzfeed
from django.http import HttpResponse

def buzzfeedSet(word):output = getBuzzfeed(word)
	return HttpResponse("DID IT WORK?")


