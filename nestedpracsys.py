#!/usr/bin/env python3
import sys
x=sys.argv[1] #get sysargv input
count=int(x) #convert sys into an integer
if count<0:
	message="is negative"
	print(count,message)
if count>0:
	message="is positive"
	print(count,message)
	if count<50:
		message="is less than 50"
		print(count,message)
		if count%2==0:
			message="is less than 50 and even"
			print(count,message)
	if count>50:
		message="is greater than 50"
		print(count,message)
		if count%2==1:
			message="is greater than 50 and odd"
			print(count,message)
else:
	message="is equal to 0"
	print(count,message)


