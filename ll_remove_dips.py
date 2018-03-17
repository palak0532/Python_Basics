#Incomplete code 

import os 
import sys


class Node1:
	def __init__(self, data):
		self.val = data
		self.next = None

	def traverse(self, count):
		num = 0
		temp = self
		while(temp != None):
			num = num+1
			if(num == count):
				print temp.val
				break
				#print "Hi"
			else:
				temp = temp.next
				
		if(num<count):
			print "Out of range"

	def len(self):
		num = 0
		temp = self
		while(temp != None):
			num = num+1
			temp = temp.next
		return num


class Node2:
	def __init__(self, data):
		self.val = data
		self.next = None






if __name__ == '__main__':
	node1 = Node1(5)
	node1.next = Node1(7)
	node1.next.next = Node1(9)

	node2 = Node2(3)
	node2.next = Node2(7)

	c1 = node1.len()
	print c1
	

	



