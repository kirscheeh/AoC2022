#!/usr/bin/env python

import sys 

data = open("input/day_13.txt").read()
pairs = data.split("\n\n")

index_pairs = {}

for index, pair in enumerate(pairs):
    left, right = pair.split("\n")
    index_pairs[index] = [eval(left), eval(right)]
    
right_order=[]

def compare_pair(left, right) -> bool:
	if isinstance(left, int) and isinstance(right, int):
		if left < right:
			return True
		else: return False
	else:
		if isinstance(left, list) and isinstance(right, list):
			if len(left) == 0 and len(right) > 0:
				return True 
			elif len(right) == 0 and len(left) > 0:
				return False
			else:
				for l_item, r_item in zip(left, right):
        

for index, (left, right)in index_pairs.items():
    
    if x:=compare_pair(left, right):
        right_order.append(index)
        
    print(left, right, x)

print(right_order)
