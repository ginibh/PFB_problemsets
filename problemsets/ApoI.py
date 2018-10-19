#!/usr/bin/env python3
import re
dna=open("Python_07_ApoI.fasta","r")
longseq=""
for line in dna:
	line=line.rstrip()
	if line.startswith(">"):
		continue
	else:
		longseq+=line
print(longseq)
ApoI_site=re.findall(r"[AG]AATT[CT]",longseq)
print(ApoI_site)			
