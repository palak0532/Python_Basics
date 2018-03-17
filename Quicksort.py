import sys
import os

Array = [10,9,8,5,11,3]

def quicksort (arr, low, high):

	start = low
	end = high
	element =(start+end)/2
	pivot = arr[element]
	


	while (start < end):

		while (arr[start] < pivot):
			start = start +1
			#print start 
		while (arr[end] > pivot):
			end = end -1
			#print end
		if(start<=end):
			arr[start] , arr[end] = arr[end] , arr [start]
			start = start +1;
			end = end -1;
	print arr
#		i
	if(low < end):
		quicksort(arr, low, end)
	if(start < high):
		quicksort(arr, start, high)
	return arr

low =0;
high = len(Array)-1;

x = quicksort(Array, low, high)

print Array