
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
from buzzfeed.models import BuzzfeedSearch
from buzzfeed.serializers import BuzzfeedSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
indicoio.config.api_key = "fd1d2b43d2cecbb5bf178f3062cd96f1"


#USE OF HASHMAPS 
def getFrequentWords(jsonStr):
	try:
		hash_map = HashMap().
		for i in jsonStr:
			for j in i:
				for item in j:
					words = str(item).split(" ")
					for word in words:
						if word != "":
							if(hash_map.containsKey(word) == False):
								hash_map.put(word, 1) 
							else:
								node =hash_map.query(word).setValue(hash_map.get(word)+1)  
				highest_value = hash_map.find_highest_value()
				for i in highest_value:
					return highest_value
	except: 
		return "None"

def getSentiment(jsonInput, word):
	jsonStr = ""
	try:
		sentiments =  indicoio.sentiment(jsonInput[0][0])
		keywords = indicoio.keywords(jsonInput[0][0])
		average =0 
		above_average = 0 
		below_average =0 
		for sentiment in sentiments: 
			average+= sentiment
			if (sentiment > 0.5) : 
				above_average = above_average+1
			else: 
				below_average=below_average+1
		average = average/len(sentiments)
		above_average = float(above_average)/len(sentiments)
		below_average= float(below_average)/len(sentiments) 
	   	most_frequent_words =getFrequentWords(jsonInput)
		jsonStr = "{\"results\":{\"above_average\":\""+str(above_average)+"\", \"word\":\""+word+"\",\"below_average\" :\""+str(below_average)+"\",\"average\":"+str(average)+"}, \"keywords\": \""+str(keywords)+"\", \"most_frequent_word\":\""
		for i in most_frequent_words[1:len(most_frequent_words)]:
			print(i.getKey())
			jsonStr+=i.getKey()+","
		jsonStr+= "\"}"

		result = BuzzfeedSearch(json=jsonStr, name=word)
		result.save()
		serializer = BuzzfeedSerializer(result)
		content = JSONRenderer().render(serializer.data) 
		all_entries = BuzzfeedSearch.objects.all()

	except Exception,e:
		return jsonStr
	return jsonStr

#Getting the text from p and h2 divs
def getText(items, jsonStr):
		url=items['url']
		html = urllib.urlopen(url).read()
		htmlObject = BeautifulSoup(html, features="html") 
		count =0
		#must do for <p tags too. 
		if  htmlObject.findAll(re.compile("h2", re.S)) != None:
			jsonStr = Parallel(n_jobs=1000) (delayed(checkH2) (item, jsonStr) for item in htmlObject.findAll(re.compile("h2", re.S)) )
		count =0
		if  len(jsonStr) < 10 or None in jsonStr: #if th jsonStr is sitl empty
			jsonStr = Parallel(n_jobs=1000) (delayed(checkP) (item, jsonStr) for item in  htmlObject.findAll("p") )
		return jsonStr

#Checkng the H2 div.
def checkH2(item, jsonStr):
	pattern = re.compile("<h2 class=\"subbuzz_nam(.*)span>(.*)", re.S)
	match= pattern.match(repr(item))
	count =0
	if count == 0:
		if match != None:
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
			if match != None:
			#	#print("MATH  C")
			#	#print(match.groups()[1]) 
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
		jsonStr.append(text)
		count = 1
	else:
		text = text.replace("\n","")
		text = text.replace('u201c', ' ')
		text = text.replace('u201d', ' ')
		text = text.replace("u2019", "'")
		text = text.replace("h2", "")
		text = text.replace("       ", "")
		text = text.replace("\r","")
		regex = re.compile('[^a-zA-Z]')
		regex.sub('', text)
		##print("Tex tinserted in is ")
		jsonStr.append(text)
	return jsonStr

#For each url, return the comments from the search results. 
def getBuzzfeedPost(input):
	jsonObj = json.loads(input)
	jsonStr= []
	count = 0; 
	jsonStr = Parallel(n_jobs=2000) (delayed(getText) (items, jsonStr) for items in jsonObj['results'])

	return jsonStr

#Entry point, parses search results page to find URL nad titles. 
def getBuzzfeed(word):
	firstNode = LinkedListNode("")
	firstNode.setNext(None)
	LLlist= LinkedList(firstNode)
	jsonStr = '{ \"results\": ['
	url = "http://www.buzzfeed.com/tag/"+word
	html = urllib.urlopen(url).read()
	htmlObject = BeautifulSoup(html, features="lxml")
	headlines = []
	count =0
	##print ("Second tag")
	##print (htmlObject)
	for item in htmlObject.findAll(re.compile("h2", re.S)):
		if count <3:
		#	#print(item)
			pattern = re.compile("<a href=\"(.*)\" rel:gt_act=\"post/titl.*>(.*)</a>", re.S)
			match = pattern.match(repr(item.a))
			if match != None:
				url = "http://www.buzzfeed.com"+match.groups()[0]
				match= match.groups()[1].replace("\\n\\t\\t\\n\\t\\t\\t","")
				match = match.replace("\\xa0", " ")
				match = match.replace('u201c', ' ')
				match = match.replace('u201d', ' ')
				match = match.replace('u2026', ' ')
				match = match.replace("\\n\\t\\t", "")
				match = re.sub(r'\W+', ' ', match)
				match = match.replace("u2019", "'")
				node = LinkedListNode(url)
				node.setTitle(match)
				LLlist.insertFirst(node)
				count= count+1
	currentJSON = LLlist.deleteFirst()
	while(currentJSON.getNext().getNext() != None):
		jsonStr+= " {\"title\": \" "+currentJSON.getTitle()+ "\", \"url\": \""+currentJSON.getURL() +"\" }, "
		currentJSON = LLlist.deleteFirst()

	jsonStr+= " {\"title\": \" "+currentJSON.getTitle()+ "\", \"url\": \""+currentJSON.getURL() +"\" } "
	jsonStr+= ' ]}'
	sentiment = getSentiment(getBuzzfeedPost(jsonStr), word) 
	return sentiment



