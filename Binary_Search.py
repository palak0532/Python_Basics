import os
import sys

A = [4, 6, 12, 56, 64, 75]


def Binary_Search(arr, i, j, key):

	low = i
	high = j

	if (high >=1):

		mid = (low + (high-1)/2)
 		piv = arr[mid]

 		if (key == piv):

 			return  mid

 		elif (key < piv):
 			return Binary_Search(arr, low, mid-1, key)

 		else:
 			return Binary_Search(arr,mid+1, high, key)
 	else :
 		return -1

 	 


length = len(A)-1

x = Binary_Search(A, 0, length, 4)


if (x == -1):
	print " Element not found in array"
else:
	print "Element found at position %d in the array" % x



