from random import *
from time import *
 
seed()
x = [10,9,8,5,11,3]

 
def qsort(x, l, r):
    i = l
    j = r
    p = x[l + (r - l) / 2] # pivot element in the middle
    while i <= j:
        while x[i] < p: i += 1
        while x[j] > p: j -= 1
        if i <= j: # swap 
            x[i], x[j] = x[j], x[i]
            i += 1
            j -= 1
    if l < j: # sort left list
        qsort(x, l, j)
    if i < r: # sort right list
        qsort(x, i, r)
    return x

start = time()
print "Before: ", x
x = qsort(x, 0, len(x) - 1)
print "After: ", x
print "%.2f seconds" % (time() - start)
