#creating the class for a hashmap 
class HashmapNode(object):

	def __init__(self, data, value): 
		self.key = data
		self.value = value

	def getKey(self):
		print("Returning "+self.key)
		return self.key

		
	def setKey(self, data): 
		self.key = data 
	def getValue(self):
		return self.value
	def setValue(self, data):
		self.value = data

	