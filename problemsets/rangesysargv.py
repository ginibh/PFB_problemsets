#!/usr/bin/env python3
import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
number_list=[num for num in range(x,y)]
print(number_list)
for num in number_list:
	if num%2!=0:
		print(num)
