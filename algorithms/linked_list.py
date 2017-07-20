class Node():
	def __init__(self, value, next):
		self.value=value
		self.next=next

class LinkedList():
	def __init__(self, head, tail):
		self.head=head
		self.tail=tail

	def add(self, node):
		self.tail.next=node
		self.tail=node

	def find(self,node):
		previous = None
		current = self.head
		while current is not None:
			previous=current
			current=current.next
			
			# print previous.value, current.value
			if current == node:
				return current, previous

	def remove(self,node):
		key,previous = self.find(node)
		# print self.find(node)
		previous.next=key.next


def main():
	new_node = Node (5,None)
	another_node=Node(6,new_node)
	third_node=Node(7,None)


	# print new_node.next
	new_linked_list = LinkedList (another_node, new_node)

	new_linked_list.add(third_node)
	ok = new_linked_list.find (new_node)
	rm= new_linked_list.remove(new_node)

	# print ok
	# for node in rm:
	# 	print node.value
# 
	# print new_linked_list.
	print new_linked_list.head.value
	print new_linked_list.head.next.value
	print new_linked_list.tail.value



if __name__ == '__main__':
  main()