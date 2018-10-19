#!/usr/bin/env python3
import re
fa=open("multiseq.fasta","r")#open file
sequence_dict={} #create an empty dictionary
longseq="" #an empty variable for value of dict
gene_name="" #a key variable for dict
for line in fa:
	line=line.rstrip()
	if line.startswith(">"):
		gene_name=line[1::] #allows printing without > 
		sequence_dict[gene_name]=''#assign key to dict
		#print(sequence_dict)
	else:
		#longseq+=line
		sequence_dict[gene_name] += line#assign value to key
print(sequence_dict) #print dict
#print(longseq)
ApoI_site=re.findall(r"[AG]AATT[CT]",longseq)
print(ApoI_site)			
