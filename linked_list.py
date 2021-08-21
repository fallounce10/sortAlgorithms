class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = Node(None)
		self.tail = Node(None)
		self.head.next = self.tail
		self.tail.next = self.head

	def add(self, data):
		newNode = Node(data)

		if self.head is None:
			self.head = self.tail = newNode
			newNode.next = self.head
		else:
			self.tail.next = newNode
			self.tail = newNode
			self.tail.next = self.head

	def display(self):
		current = self.head
		
		if self.head is None:
			return "Empty List"
		else:
			while current.next != self.head:
				current = current.next
				print(current.data)
