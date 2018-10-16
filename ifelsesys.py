#!/usr/bin/env python3
import sys
str=sys.argv[1]
count=int(str)
if count>50:
	message="greater than 50"
	print(count,message)
else:
	message="less than 50"
	print(count,message)
