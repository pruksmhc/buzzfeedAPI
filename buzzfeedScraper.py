
import sys
import urllib
from bs4 import BeautifulSoup
import re
import json
from LinkedListNode import LinkedListNode
from Linked_List import LinkedList
import indicoio
from ast import literal_eval




#return an API. 


#r = requests.get("http://www.buzzfeed.com/tag/america") 
#r.headers['content-type']
#'text/html'
#r.encoding
#'ISO-8859-1'
#r.apparent_encoding
#'utf-8'
#extract the urls from the json and open them one by one. 


indicoio.config.api_key = "fd1d2b43d2cecbb5bf178f3062cd96f1"

#	jsonObj = json.loads("[{\"url\": \"http://www.buzzfeed.com/bradesposito/not-today-movie\", \"title\": \" No There Won 't Be A Game Of Thrones Movie Any Time Soon\"}]"


def getSentiment(json):
	array = literal_eval(json)
	sentiments =  indicoio.sentiment(array)
	print(sentiments)
	average =0 
	above_average = 0 
	below_average =0 
	for sentiment in sentiments: 
		average+= sentiment
		if(sentiment > 0.5): 
			print("Above average")
			above_average = above_average+1
		else: 
			print("Below")
			below_average=below_average+1

	average = average/len(sentiments)
	print average #this gets the average, you want to get the d3 to get the 
	#total amoutn of poercentage who has a sentiment above 0.5 is good
	print (str(above_average))
	above_average = float(above_average)/len(sentiments)
	print(str(below_average))
	print (len(sentiments))
	below_average= float(below_average)/len(sentiments)

	json = "{\"results\":[ \""+str(above_average)+"\", \""+str(below_average)+"\", \""+str(average)+"\"]}"
	print json
	return json


def getBuzzfeedPost(input):
	print(input)
	print("GETTING TO GET BUZZFEED POST")
	jsonObj = json.loads(input)
	jsonStr="["
	print(jsonObj['results'])
	count = 0; 
	for items in jsonObj['results']:
		print("First item is ")
		print(items)
		print(items['url'])
		url=items['url']
		html = urllib.urlopen(url).read()
		htmlObject = BeautifulSoup(html, features="html") 
		print("Opening hte first url")
		print(htmlObject)
		for item in htmlObject.findAll(re.compile("h2", re.S)):
			pattern = re.compile("<h2 class=\"subbuzz_nam(.*)span>(.*)", re.S)
			match= pattern.match(repr(item))
			if count == 0:
				if match != None:
					print(match.groups()[1]) 
					match= match.groups()[1].replace("\\n\\t\\t\\n\\t\\t\\t","")
					match = match.replace("\\xa0", " ")
					match = match.replace('u201c', ' ')
					match = match.replace('u201d', ' ')
					match = match.replace("\\n\\t\\t", "")
					match = re.sub(r'\W+', ' ', match)
					match = match.replace("u2019", "'")
					match = match.replace("h2", "")
					match = match.replace("u2026", "")
					jsonStr+="\""+match +"\""
					count =1
			else:
				print("Now, looking at this item for h2")
				print (item)
				if match != None:
					print("MATH  C")
					print(match.groups()[1]) 
					match= match.groups()[1].replace("\\n\\t\\t\\n\\t\\t\\t","")
					match = match.replace("\\xa0", " ")
					match = match.replace('u201c', ' ')
					match = match.replace('u201d', ' ')
					match = match.replace("\\n\\t\\t", "")
					match = re.sub(r'\W+', ' ', match)
					match = match.replace("u2019", "'")
					match = match.replace("h2", "")
					jsonStr+=", \""+match +"\""

	jsonStr+="]"
	print jsonStr
	return jsonStr


print ("PRINTING BUZZFEE")

firstNode = LinkedListNode("")
firstNode.setNext(None)
LLlist= LinkedList(firstNode)
jsonStr = '{ \"results\": ['
url = "http://www.buzzfeed.com/tag/America"
html = urllib.urlopen(url).read()
htmlObject = BeautifulSoup(html, features="lxml")
headlines = []
count =0
print ("Second tag")
print (htmlObject)
for item in htmlObject.findAll(re.compile("h2", re.S)):
	if count <3:
		print(item)
		pattern = re.compile("<a href=\"(.*)\" rel:gt_act=\"post/titl.*>(.*)</a>", re.S)
		match = pattern.match(repr(item.a))
		print(match==None)
		if match != None:
			url = "http://www.buzzfeed.com"+match.groups()[0]
			print(url)
			match= match.groups()[1].replace("\\n\\t\\t\\n\\t\\t\\t","")
			match = match.replace("\\xa0", " ")
			match = match.replace('u201c', ' ')
			match = match.replace('u201d', ' ')
			match = match.replace("\\n\\t\\t", "")
			match = re.sub(r'\W+', ' ', match)
			match = match.replace("u2019", "'")
			print(match)
			node = LinkedListNode(url)
			node.setTitle(match)
			print("The node is "+node.getURL())
			print ("The title is "+node.getTitle())
			LLlist.insertFirst(node)
			print("The  next object is "+ LLlist.getHead().getNext().getURL())
			count= count+1

	#appending to the JSOn to return it back. 
currentJSON = LLlist.deleteFirst()
while(currentJSON.getNext().getNext() != None):
	print ("The current json is "+currentJSON.getTitle())
	jsonStr+= " {\"title\": \" "+currentJSON.getTitle()+ "\", \"url\": \""+currentJSON.getURL() +"\" }, "
	currentJSON = LLlist.deleteFirst()

		#if the last node 
jsonStr+= " {\"title\": \" "+currentJSON.getTitle()+ "\", \"url\": \""+currentJSON.getURL() +"\" } "
jsonStr+= ' ]}'
print (jsonStr)
commentsList = getBuzzfeedPost(jsonStr)
sentiment = getSentiment(commentsList)
#create a hhahmap with teh most used words. 
return sentiment 



	
	#then you want to parse it through an Indico API. 
	#return a list of ocmments from Buzzfeed. 





		#now, you want to create a new linked list, with the data being 


