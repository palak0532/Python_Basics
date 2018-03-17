


import sys
import os

def str():
	s ="palak malhotra"
	chars = []

	for i, alpha in enumerate(s):
		
		if (alpha in chars):
			return False
		chars.append(alpha)
	return True





if __name__ == '__main__':
	S = str()
	if S == True:
		print "String has all unique characters"
	else:
		print "string has duplicates"
        