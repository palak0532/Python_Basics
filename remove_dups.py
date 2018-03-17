import sys
import os

string = "uuuuuuuuuuuuuuu"

setA=list(string)
setB=[]


for y, x in enumerate(setA):
	if x not in setB:
		setB.append(x)

print ''.join(setB)