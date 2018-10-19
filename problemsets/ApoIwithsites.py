#!/usr/bin/env python3
import re
dna=open("Python_07_ApoI.fasta","r")#open file
longseq=""#start a string empty
for line in dna:
	line=line.rstrip()
	if line.startswith(">"):
		continue #continue after seeing a line with >
	else:
		longseq+=line #concatenate line to get one dna string
print(longseq)
ApoI_site=re.findall(r"[AG]AATT[CT]",longseq)#find all sites
print(ApoI_site)			
for sites in re.finditer(r"([AG]AATT[CT])",longseq):#another way to list sites
	print(sites.group())
new_longseq=re.sub(r'([AG])(AATT[CT])',r"\1^\2",longseq)#setting groups with parantheses and then using groups to replace
print(new_longseq) 
Cut_products=new_longseq.split('^')
size_cut=sorted(Cut_products,key=len,reverse=True)
print(size_cut)
