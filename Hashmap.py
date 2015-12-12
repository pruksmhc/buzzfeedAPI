from hashmapnode import HashmapNode 

class HashMap(object):


	def __init__(self): 
		self.nodeList=[]

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


#Finds highest value in the hashmap. 
	def find_highest_value(self):
		#finds the top result right
		current_node = None
		count =0
		list_highest=[] 
		print("IN EHRE ") 
		sorted_list = sorted(self.nodeList, key=lambda node: node.value,  reverse=True)

		if len(self.nodeList) < 10:
			return self.nodeList

		for node in sorted_list: 
			if count <10: 
				print(node.getValue())
				list_highest.append(node) 
				count = count+1 
			else:
				break

		return list_highest


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
		if(key.isalnum()):
			key = key.replace("?", "")
			node  = HashmapNode(key, value)
			#print("the nde's key being inserted in is "+node.getKey())
			self.nodeList.append(node)
		#	print("WOAH")
		


