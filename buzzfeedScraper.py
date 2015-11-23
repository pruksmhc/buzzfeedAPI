
import sys
import urllib
from bs4 import BeautifulSoup
import re
import json
from LinkedListNode import LinkedListNode
from Linked_List import LinkedList




#return an API. 


#r = requests.get("http://www.buzzfeed.com/tag/america") 
#r.headers['content-type']
#'text/html'
#r.encoding
#'ISO-8859-1'
#r.apparent_encoding
#'utf-8'
def getBlogContent(jsonObj):
#extract the urls from the json and open them one by one. 
jsonObj = json.loads("[{\"url\": \"http://www.buzzfeed.com/bradesposito/not-today-movie\", \"title\": \" No There Won 't Be A Game Of Thrones Movie Any Time Soon\"}]"
)
jsonStr="["
print(jsonObj)
for items in jsonObj:
jsonStr+="{"
print(items)
print(items['url'])
url=items['url']
html = urllib.request.urlopen(url).read()
htmlObject = BeautifulSoup(html, features="html") 
print(htmlObject)
for item in htmlObject.findAll(re.compile("h2", re.S)):
print (item)
pattern = re.compile("<h2 class=\"subbuzz_nam(.*)span>(.*)", re.S)
match = pattern.match(repr(item))
if(match != None):
print("MATHC")
print(match.groups()[1])
jsonStr+=match.groups()[1] +","
jsonStr+="},"




def getBuzzfeed(word): 

firstNode = LinkedListNode("")
firstNode.setNext(None)
LLlist= LinkedList(firstNode)
jsonStr = '['
url = "http://www.buzzfeed.com/tag/"+word
html = urllib.urlopen(url).read()
htmlObject = BeautifulSoup(html, features="lxml")
headlines = []
for item in htmlObject.findAll(re.compile("h2", re.S)):
#print repr(item.a)
pattern = re.compile("<a href=\"(.*)\" rel:gt_act=\"post/titl.*>(.*)</a>", re.S)
match = pattern.match(repr(item.a))
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

#appending to the JSOn to return it back. 
currentJSON = LLlist.deleteFirst()
while(currentJSON.getNext().getNext() != None):
print ("The current json is "+currentJSON.getTitle())
jsonStr+= " {\"title\": \" "+currentJSON.getTitle()+ "\", \"url\": \""+currentJSON.getURL() +"\" }, "
currentJSON = LLlist.deleteFirst()

#if the last node 
jsonStr+= " {\"title\": \" "+currentJSON.getTitle()+ "\", \"url\": \""+currentJSON.getURL() +"\" } "
jsonStr+= ' ]'
print (json.dumps(jsonStr))





#now, you want to create a new linked list, with the data being 


print ("Done")


#print soup.get_text()
