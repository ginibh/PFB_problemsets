#!/usr/bin/env python3
count=66
if count<0:
	message="is negative"
	print(count,message)
elif count>0:
	message="is positive"
	print(count,message)
	if count<50:
		message="is less than 50"
		print(count,message)
		if count%2==0:
			message="it is an even number that is less than 50"
			print(count, message)
	if count>50:
		message="is greater than 50"
		print(count,message)
		if count%3==0:
			message="it is divisible by 3 and greater than 50"
			print(count,message)
else:
	message="is 0"
	print(count,message)

