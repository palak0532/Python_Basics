import io
import os
import sys

A = [25,22,12,3,11,89,3]

for i in range(len(A)):
    
    min_i = i
    for j in range(i+1, len(A)):
        if A[min_i] > A[j]:
            min_i = j
             
    # Swap the found minimum element with 
    # the first element        
    A[i], A[min_i] = A[min_i],A[i]

print A;
