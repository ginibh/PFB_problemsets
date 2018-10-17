#!/usr/bin/env python3
numbers=[101,2,15,22,95,33,2,27,72,15,52]
sum_even=0
sum_odd=0
for num in numbers:
	if num%2==0:
		sum_even+=num
	else: 
		sum_odd+=num
print(sum_even)
print(sum_odd)	
		
