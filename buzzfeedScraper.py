
import sys
import urllib
import urllib3
import certifi
from bs4 import BeautifulSoup
import re
import json
from LinkedListNode import LinkedListNode
from Linked_List import LinkedList
import indicoio
from ast import literal_eval
from Hashmap import HashMap 
from joblib import Parallel, delayed
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()
import multiprocessing


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


def getFrequentWords(jsonStr):
	#	print("PRINTING MOST FREQUENT WORD ")
	
	try:
		print("In here")
		print(type(jsonStr))
		hash_map = HashMap("hello")

		for i in jsonStr:
			for j in i:
				for item in j:
					print("The items are "+item)
					words = str(item).split(" ")

	#		print (words)
					for word in words:
						if word != "":
			#		print("The word being examined is "+word)

							if(hash_map.containsKey(word) ==False):
				#		print("Putitng the word in")
								print("Inserting for first time"+ word)

								hash_map.put(word, 1) 
							else:
								print("Inserting and incrementing"+ word)
				#		print("Incrementing the word")
								node =hash_map.query(word).setValue(hash_map.get(word)+1)  
				#at the end fo the array 
	#	print (hash_map.find_highest_value().getKey())
				print("STIL HERE")

				highest_value = hash_map.find_highest_value()
				print(type(highest_value))
				for word in highest_value:
					print("HIGHEST "+word)
				return highest_value
	except: 
		print(sys.exc_info()[0])
		print("Reutrning none")
		return "None"

def getSentiment(jsonInput):
	jsonStr = ""
#	print("Getitng the sentiment")

#	print(json[0][0])

	try:
	#	print("EVALUATED ARRAY")
		sentiments =  indicoio.sentiment(jsonInput[0][0])
	#	print("has gotten the snetimetns, getitng keyw ords")
		keywords = indicoio.keywords(jsonInput[0][0])
	#	print(sentiments)
	#most frequent words. 


		average =0 
		above_average = 0 
		below_average =0 
		for sentiment in sentiments: 
			average+= sentiment
			if(sentiment > 0.5): 
		#		print("Above average")
				above_average = above_average+1
			else: 
			#	print("Below")
				below_average=below_average+1

		average = average/len(sentiments)
	#	print average #this gets the average, you want to get the d3 to get the 
		#total amoutn of poercentage who has a sentiment above 0.5 is good
		above_average = float(above_average)/len(sentiments)
		below_average= float(below_average)/len(sentiments) 
		print("GETTING REQUENT WORKS")
	   	most_frequent_words =getFrequentWords(jsonInput) 
	#	print('Most frequtent word is '+ most_frequent_words)
	    	words_string=''.join(most_frequent_words)

		jsonStr = "{\"results\":{\"above_average\":\""+str(above_average)+"\", \"below_average\" :\""+str(below_average)+"\",\"average\":"+str(average)+"}, \"keywords\": \""+str(keywords)+"\", \"most_frequent_word\":\""
		for i in most_frequent_words[1:len(most_frequent_words)]:
			jsonStr+=i+","
		jsonStr+= "\"}"
				


	except Exception,e:
	#	print "Unexpected error:", sys.exc_info()[0]
	 #  	print str(e)
	#	print ("Whoops, there was an eror, returning empty json stirng")
	#	print jsonStr
		return jsonStr
#	print jsonStr
	return jsonStr

def getJSON(items, jsonStr):
	#this is where i need to parallelize the process. 
	#	print("First item is ")
	#	print(items)
	#	print(items['url'])
		url=items['url']
		html = urllib.urlopen(url).read()
		htmlObject = BeautifulSoup(html, features="html") 
	#	print("Opening hte first url")
	#	print(htmlObject)
		#if it can find it. 
		count =0
		#must do for <p tags too. 
		if  htmlObject.findAll(re.compile("h2", re.S)) != None:
			#msut ask if t it is equal to none.
		#	print("getting here ")
		#	print( htmlObject.findAll(re.compile("h2", re.S)))
			jsonStr = Parallel(n_jobs=7) (delayed(checkH2) (item, jsonStr) for item in htmlObject.findAll(re.compile("h2", re.S)) )

				
		count =0
		if  len(jsonStr) < 10 or None in jsonStr: #if th jsonStr is sitl empty
		#here ou check fo rthe p. 
			jsonStr = Parallel(n_jobs=1000) (delayed(checkP) (item, jsonStr) for item in  htmlObject.findAll("p") )

		return jsonStr

def checkH2(item, jsonStr):
#	print("The item being examined is ")
#	print(type(item))
	pattern = re.compile("<h2 class=\"subbuzz_nam(.*)span>(.*)", re.S)
	match= pattern.match(repr(item))
	count =0
#	print("Still here?")
	if count == 0:
		if match != None:
		#	print("Match is not none")
		#	print(match.groups()[1]) 
			match= match.groups()[1].replace("\\n\\t\\t\\n\\t\\t\\t","")
			match = match.replace("\\xa0", " ")
			match = match.replace('u201c', ' ')
			match = match.replace('u201d', ' ')
			match = match.replace("\\n\\t\\t", "")
			match = re.sub(r'\W+', ' ', match)
			match = match.replace("u2019", "'")
			match = match.replace("h2", "")
			match = match.replace("u2026", "")
			jsonStr.append(match)
			count =1
		else:
			print("Now, looking at this item for h2")
			if match != None:
			#	print("MATH  C")
			#	print(match.groups()[1]) 
				match= match.groups()[1].replace("\\n\\t\\t\\n\\t\\t\\t","")
				match = match.replace("\\xa0", " ")
				match = match.replace('u201c', ' ')
				match = match.replace('u201d', ' ')
				match = match.replace("\\n\\t\\t", "")
				match = re.sub(r'\W+', ' ', match)
				match = match.replace("u2019", "'")
				match = match.replace("h2", "")
				jsonStr.append(match)
	return jsonStr

def checkP(item, jsonStr):
	#print("CHECKING ")
	text= item.text
	count =0
	if count == 0:
		text = text.replace("\n","")
		text = text.replace("\t","")
		text = text.replace("\\xa0", " ")
		text = text.replace('u201c', ' ')
		text = text.replace('u201d', ' ')
		text = text.replace("u2019", "'")
		text = text.replace("h2", "")
		text = text.replace("\a","")
		text = text.replace("\"","")
		text = text.replace("\'","")
		regex = re.compile('[^a-zA-Z]')
		regex.sub('', text)
	#	print("Tex tinserted in is ")
		jsonStr.append(text)
		count = 1
	else:
	#	print("inserting")
		text = text.replace("\n","")
		text = text.replace('u201c', ' ')
		text = text.replace('u201d', ' ')
		text = text.replace("u2019", "'")
		text = text.replace("h2", "")
		text = text.replace("       ", "")
		text = text.replace("\r","")
		regex = re.compile('[^a-zA-Z]')
		regex.sub('', text)
		#print("Tex tinserted in is ")
	#	print(text)
		jsonStr.append(text)
	#	print("fINISHED")
	return jsonStr

def getBuzzfeedPost(input):
#	print(input)
#	print("GETTING TO GET BUZZFEED POST")
	jsonObj = json.loads(input)
	jsonStr= []
#	print(jsonObj['results'])
	count = 0; 
	#parallizing the for-loop to get the h2. 
	jsonStr = Parallel(n_jobs=2) (delayed(getJSON) (items, jsonStr) for items in jsonObj['results'])
	
			
				 #This is now getitng the p tags. 
			

	#print("Returning json")
	#print(jsonStr)
	try:
		for i in jsonStr:
			for j in i:

				for k in j:
					print("By the time you get the json String, the buzzfeed post should be "+k) 
					print(type(k))

	except:
		print(sys.exc_info()[0])

	return jsonStr

def getBuzzfeed(word):
	#print ("PRINTING BUZZFEE")
	print(word)

	firstNode = LinkedListNode("")
	firstNode.setNext(None)
	LLlist= LinkedList(firstNode)
	jsonStr = '{ \"results\": ['
	url = "http://www.buzzfeed.com/tag/"+word
	html = urllib.urlopen(url).read()
	htmlObject = BeautifulSoup(html, features="lxml")
	headlines = []
	count =0
	#print ("Second tag")
	#print (htmlObject)
	for item in htmlObject.findAll(re.compile("h2", re.S)):
		if count <3:
		#	print(item)
			pattern = re.compile("<a href=\"(.*)\" rel:gt_act=\"post/titl.*>(.*)</a>", re.S)
			match = pattern.match(repr(item.a))
		#	print(match==None)
			if match != None:
				url = "http://www.buzzfeed.com"+match.groups()[0]
			#	print(url)
				match= match.groups()[1].replace("\\n\\t\\t\\n\\t\\t\\t","")
				match = match.replace("\\xa0", " ")
				match = match.replace('u201c', ' ')
				match = match.replace('u201d', ' ')
				match = match.replace('u2026', ' ')
				match = match.replace("\\n\\t\\t", "")
				match = re.sub(r'\W+', ' ', match)
				match = match.replace("u2019", "'")
			#	print(match)
				node = LinkedListNode(url)
				node.setTitle(match)
		#		print("The node is "+node.getURL())
		#		print ("The title is "+node.getTitle())
				LLlist.insertFirst(node)
		#		print("The  next object is "+ LLlist.getHead().getNext().getURL())
				count= count+1

		#appending to the JSOn to return it back. 
	currentJSON = LLlist.deleteFirst()
	while(currentJSON.getNext().getNext() != None):
		#print ("The current json is "+currentJSON.getTitle())
		jsonStr+= " {\"title\": \" "+currentJSON.getTitle()+ "\", \"url\": \""+currentJSON.getURL() +"\" }, "
		currentJSON = LLlist.deleteFirst()

			#if the last node 
	jsonStr+= " {\"title\": \" "+currentJSON.getTitle()+ "\", \"url\": \""+currentJSON.getURL() +"\" } "
	jsonStr+= ' ]}'
#	print (jsonStr)
	#print("KIn teh kgetBuzzfeed post")
	sentiment = getSentiment(getBuzzfeedPost(jsonStr)) 
	#print("returning sentiment")
	print("Returning for good")
	return sentiment

	#create a hhahmap with teh most used words. 



		
		#then you want to parse it through an Indico API. 
		#return a list of ocmments from Buzzfeed. 





			#now, you want to create a new linked list, with the data being 


