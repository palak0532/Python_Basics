import sys
import os

A = [3,7,83,45,12,66]

for i in xrange(1,len(A)):

	pivot = A[i]

	j = i-1

	while( j>=0 and pivot < A[j]):
		A[j+1] = A[j]
		j = j-1

	A[j+1]=pivot

print A

