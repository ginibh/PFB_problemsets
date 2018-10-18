#!/usr/bin/env python3
import re
fasta=open("Python_07.fasta","r")
header=open("fastaheader.txt","w")
for line in fasta:
	line=line.strip()
	if line.startswith('>'):
		gene=re.findall(r">\S+.+",line)
		print(gene)
		ID ="".join(gene)
		header.write(ID)
		print(ID)
print("Done")
