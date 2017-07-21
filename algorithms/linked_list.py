class Node:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

	def __repr__(self):
		return "Node(value={}, next={})".format(self.value, self.next)

class LinkedList:
	def __init__(self, head):
		self.head = head
		self.tail = self.set_tail()

	def __repr__(self):
		return "LinkedList(head={}, tail={})".format(self.head, self.tail)

	def set_tail(self):
		# finds the last node in the head
		current_node = self.head
		while current_node and current_node.next:
			current_node = current_node.next
		return current_node

	def add(self, new_node):
		if self.tail:
			old_tail = self.tail
			old_tail.next = new_node
			self.tail = new_node
		else:
			self.head.next = new_node
			self.tail = new_node

		# because new_node could have many other nodes linked to it
		# we need to find the very last node and make that the tail
		while self.tail.next:
			self.tail = self.tail.next

	def find(self,node):
		previous = None
		current = self.head
		# check if current node is the one we want before moving to next
		# (otherwise this will not find the head node)
		while current is not None:
			if current == node:
				return current, previous
			else:
				previous = current
				current = current.next

	def remove(self,node):
		key, previous = self.find(node)
		previous.next = key.next

def main():
	new_node = Node (6)
	another_node = Node(5, new_node)
	fourth_node = Node(8)
	third_node = Node(7, fourth_node)

	new_linked_list = LinkedList(another_node)
	new_linked_list.add(third_node)
	print new_linked_list # should be 5 -> 6 -> 7 -> 8 with tail of 8

	ok = new_linked_list.find(third_node)
	rm= new_linked_list.remove(third_node)
	print new_linked_list # should be 5 -> 6 -> 8 with tail of 8

if __name__ == '__main__':
  main()
