from hashmapnode import HashmapNode 

class HashMap(object):

	nodeList =[]
	def __init__(self, key): 
		self.key = key


	def containsKey(self, key): 
		for node in self.nodeList: 
	 		if node.getKey() == key:
	 			return True

	 	return False


	def query(self, key): 
		for node in self.nodeList: 
	 		if node.getKey() == key:
	 			return node

	 	return None

	def get(self, key): 
		for node in self.nodeList: 
	 		if node.getKey() == key:
	 			return node.getValue()

	 	return None


	def find_highest_value(self):
		#finds the top result right
		current_node = None
		count =0
		for node in self.nodeList: 
			if node.getValue() > count:
			#	print("the count has shifted")
				count = node.getValue()
			#	print("The count is now "+ str(count))
				current_node= node 
				print("And hte curernt nod eis "+node.getKey())
		return current_node


	def containsValue(self, value):
		for node in self.nodeList: 
	 		if node.getValue() == value:
	 			return True

	 	return False

	def isEmpty(self):
		return len(self.nodelist) == 0 

	def remove(key):
	 	for node in self.nodeList: 
	 		if node.getKey() == key: 
	 			self.nodeList.remove(key)

  #delete all occurances o hte key .

	def put(self, key, value):
		key = key.replace("?", "")
		node  = HashmapNode(key, value)
		print("the nde's key being inserted in is "+node.getKey())
		self.nodeList.append(node)

