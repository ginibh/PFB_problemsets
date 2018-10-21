#!/usr/bin/env python3
import re
fa=open("Python_08.fasta","r")#open file
sequence_dict={} #create an empty dictionary
longseq="" #an empty variable for value of dict
gene_name="" #a key variable for dict
for line in fa:
	line=line.rstrip()
	if line.startswith(">"):
		longseq=""
		gene_name=line[1::] #allows printing without > 
	else:
		longseq+=line	
		sequence_dict[gene_name] = longseq #assign value to key
print(sequence_dict)
nt_composition={}
for ID in sequence_dict:
	seq=sequence_dict[ID]
	countA=0
	countT=0
	countC=0
	countG=0
	for nt in seq:
		if nt == 'T':
			countT+=1
		elif nt == 'A':
			countA+=1
		elif nt == 'G':
			countG+=1
		else:
			countC+=1
		print(countT,countA,countG,countC)
		#print(sequence_dict)
