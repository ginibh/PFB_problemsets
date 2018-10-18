#!/usr/bin/env python3
import re
fasta=open("Python_07.fasta","r")
for line in fasta:
	line=line.rstrip()
	#if line.startswith(">"):
	for found in re.finditer(r">(\S+)\s(.+)",line): #use  a for loop. otherwise this doesn't work	
		#found=re.findall(r"(\S+)(.+)",line)
			ID=found.group(1)
			description=found.group(2)
			print("ID:",ID)
			print("Description:",description)
print("All done")
