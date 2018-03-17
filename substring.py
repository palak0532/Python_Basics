import sys
import os

class Node:
	def __init__(self, idata):
		self.data = idata
		self.next = None

	def _get_data(self):
		temp = self
		while(temp != None):
			print temp.data
			temp = temp.next
	def remove_dups(self):
		first = self
		second = self
		

		while(first != None):
			while(second.next != None):
				if(first.data == second.next.data):
					second.next = second.next.next
				else:
					second = second.next
			first = second = first.next

		self._get_data()
	def move_data(self,num):
		first = self
		second = self
		flag = 0
		temp = None
		

		while(first.next != None):
				if(first.data == num):
					print first.data
					temp = first
					first.next = first.next.next
					flag = 1
					break
				else:
					first = second.next
		if (flag == 1):
			while (second != None):
				second = second.next
			second = temp
			second.next = None

		self._get_data()


node1 = Node(4)
node2 = Node(7)
node3 = Node(4)
node4 = Node(17)

node1.next = node2
node2.next = node3
node3.next = node4

node1._get_data()
#node1. remove_dups()
#node1.move_data(7)

