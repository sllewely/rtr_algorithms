class Node():
	def __init__(self, value, prev):
		self.value=value
		self.prev=prev
		
class Stack():
	def __init__(self, top):
		self.top=top
	
	def isEmpty(self):
		if self.top is None:
			return True

	def peek(self):
		return self.top.value

	def push(self, node):
		#check if it's empty <- Sarah's solution
		node.prev=self.top
		self.top=node
		
	def pop(self):
		if self.isEmpty()is None:
			temp=self.top
			self.top=self.top.prev
			return temp

def main():
	new_node = Node (5,None)
	second_node=Node(6,new_node)
	third_node=Node(7,second_node)
	fourth_node=Node(8,third_node)

	new_stack = Stack(new_node)

	new_stack.push(second_node)
	new_stack.push(third_node)
	new_stack.push(fourth_node)
	
	print new_stack.peek()

# Question: if I return temp up in def, how can I print its value vs just calling a function?
	
	new_stack.pop()
	print new_stack.peek()

	

if __name__ == '__main__':
  main()
  #TODO
  #REVERSE A STRING