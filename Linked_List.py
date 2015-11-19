from LinkedListNode import LinkedListNode

class LinkedList(object):


	def __init__(self, head): 
		self.head =head 

	def getHead(self):
		return self.head 
	def setHead(self, head):
		self.head= head

	def insertFirst(self, LLNode): 
		if self.getHead() == None: 
			head = LLNode 
			head.setNext(None)
		else: 
			LLNode.setNext(head) 
			tail = head 
			head = lLNode

	def insertLast(self, LLnode): 
		tail.setNext(LLNode)
		tail = LLNode 
		tail.setNext(None)

	def deleteFirst(self): 
		temp = self.head
		self.head = self.head.getNext() 
		return head #insert the first, and then delete first into the json. 
		
	def query(self,  data):
		current = head 
		while(current != None):
			if current.getData() == data:
				return current 

		return None 



	def insertAfter(self, node, data):
		LLNode = LinkedListNode(data)
		lLNode.setNext(node.getNext().getNext())
		node.setNext(lLNode) 
		if node == head: 
			lLNode = tail 


   


