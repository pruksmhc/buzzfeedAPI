class LinkedListNode(object):
	#LLNodes have a next pointer and data 

	def __init__(self, data): 
		self.url = data

	def getNext(self):
		return self.next

		
	def setNext(self, next): 
		self.next = next 
	def getURL(self):
		return self.url
	def setURL(self, data):
		self.url = data 

	def setTitle(self, data):
		self.title=data
	def getTitle(self):
		return self.title