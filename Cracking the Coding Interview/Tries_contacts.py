 	"""solve the contacts problem. modified from the java version answer in the video of Gayle Laakmann McDowell"""
	
class Node(object):

	__slots__ = ['count', 'children'] 	#Space is saved because __dict__ is not created for each instance.
 	def __init__(self):
 		self.children = [None] * 26
 		self.count = 0

	def getCharIndex(self, char):
		return ord(char) - ord('a')

	def getNode(self, char):
		return self.children[self.getCharIndex(char)]

	def setNode(self, char, node):
		self.children[self.getCharIndex(char)] = node

	def add(self, string, index = None):
		if index == None:
			index = 0

		self.count += 1	
		if index == len(string):
			return

		char = string[index]
		child = self.getNode(char)
		if child == None:
			child = Node()
			self.setNode(char, child)

		child.add(string, index + 1)

	def findCount(self, string, index = None):
		if index == None:
			index = 0

		if index == len(string):
			return self.count
		char = string[index]
		child = self.getNode(char)
		if child == None:
			return 0

		return child.findCount(string, index + 1)   
n = 4
l = [['add', 'hack'], ['add', 'hackerrank'], ['find', 'hac'], ['find', 'hak']]
node = Node()
for a0 in xrange(n):
    # op, contact = raw_input().strip().split(' ')
    op, contact = l[a0]
    if op == 'add':
        node.add(contact)
    if op == 'find':
        print node.findCount(contact)

