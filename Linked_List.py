import LinkedListNode import LinkedListNode

class LinkedList(object):
	LinkedListNode head 
	LinkedListNode tail

	def __init__(self, head): 
		self.head =head 

	def getHead(self):
		return head 

	def insertFirst(self, data): 
		LLNode = new LinkedListNode(data)
		if getHead() == None: 
			head = LNode 
			head.setNext(None)
		else: 
			LLNode.setNext(head) 
			tail = head 
			head = lLNode

	def insertLast(self, data): 
		LLNode = new LinkedListNode(data)
		tail.setNext(lLNode)
		tail = LLNode 
		tail.setNext(None)

	def query(self,  data):
		current = head 
		while(current != None):
			if current.getData() == data:
				return current 

		return None 

	def insertAfter(self, node, data):
		LLNode = new LinkedListNode(data)
		lLNode.setNext(node.getNext().getNext())
		node.setNext(lLNode) 
		if node == head: 
			lLNode = tail 

    def deleteAfter(self, node):
    	node.setNext(node.getNext.getNext) 


