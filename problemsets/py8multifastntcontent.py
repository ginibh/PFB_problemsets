#!/usr/bin/env python3
import re
fa=open("Python_08.fasta","r")#open file
sequence_dict={} #create an empty dictionary
longseq="" #an empty variable for value of dict which is the sequence
gene_name="" #a key variable for dict
for line in fa:
	line=line.rstrip()#strip line of spaces at end
	if line.startswith(">"):#if line starts with >
		longseq="" #longseq remains empty.also resets for the second loop
		gene_name=line[1::] #allows printing without > 
		sequence_dict[gene_name] = {'A':0,'T':0,'G':0,'C':0} #assign value to key which in this case is a dictionary in a dictionary
	else:
		longseq+=line	#longseq=concatenate line. we can't count using longseq because of the way it adds lines. we would count A in ATG and in ATG+AG instead of total ATGAG so it owuld double count
		sequence_dict[gene_name]['A']+=line.count('A') #add a value to the dicitonary in the dictionary. for every line, 
		sequence_dict[gene_name]['T']+=line.count('T')
		sequence_dict[gene_name]['G']+=line.count('G')
		sequence_dict[gene_name]['C']+=line.count('C')
print(sequence_dict) #print dictionary
