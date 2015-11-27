from hashmapnode import HashMapNode 

class Hashmap(object):

	nodeList =[]
	def __init__(self): 

	def containsKey(self, key): 
		for node in nodeList: 
	 		if node.getKey() == key:
	 			return true

	 	return false


	def get(self, key): 
		for node in nodeList: 
	 		if node.getKey() == key:
	 			return node.getValue()

	 	return None



	def containsValue(self, value):
		for node in nodeList: 
	 		if node.getValue() == value:
	 			return true

	 	return false

	def isEmpty(self):
		return len(nodelist) == 0 

	def remove(key):
	 	for node in nodeList: 
	 		if node.getKey() == key: 
	 			nodeList.remove(key)

  #delete all occurances o hte key .

	def put(self, key, value):
		node  = HashMap(key, value)
		nodeList.append(node)
