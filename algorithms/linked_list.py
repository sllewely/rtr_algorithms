class Node:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

	def __repr__(self):
		return "Node(value={}, next={})".format(self.value, self.next)

class LinkedList:
	def __init__(self, value):
		self.head = Node(value)
		self.tail = None

	def __repr__(self):
		return "LinkedList(head={}, tail={})".format(self.head, self.tail)

	def add(self, value):
		new_node = Node(value)
		if self.tail:
			old_tail = self.tail
			old_tail.next = new_node
		else:
			self.head.next = new_node

		self.tail = new_node

	def find(self, value):
		previous = None
		current = self.head
		# check if current node is the one we want before moving to next
		# (otherwise this will not find the head node)
		while current is not None:
			if current.value == value:
				return current, previous
			else:
				previous = current
				current = current.next

	def remove(self, value):
		key, previous = self.find(value)
		previous.next = key.next

def main():
	my_list = LinkedList(1)
	print my_list

	for i in xrange(2,5):
		my_list.add(i)
		print my_list

	my_list.remove(3)
	print my_list

if __name__ == '__main__':
  main()
