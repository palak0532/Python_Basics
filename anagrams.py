from collections import Counter
import sys
import os





def anagram_check(string):
	dictionary ={}
	for item in string:
		dictionary[item] = dictionary.get(item,0)+1

	return dictionary

def is_anagram(a, b):

    return anagram_check(a.lower()) == anagram_check(b.lower())

if __name__ == '__main__':
	str1 = raw_input('Enter string 1 to be validated : ')
	str2  = raw_input('Enter string 2 to be validated : ')
	x = is_anagram(str1, str2)
	print x
		 