#!/usr/bin/env python3
import re
fa_open=open("human_cds.fasta","r") #open the file
sequence_dict={} #create an empty dictionary
gene_name="" #gene name key
for line in fa_open:#for every line
	line=line.rstrip() #strip line to get rid of empty space
	if line.startswith(">"): #if line starts with >
		gene_name=line[1::] #collect gene name
		sequence_dict[gene_name]={}	#make sure the dictionary knows that the value is empty
		nt_count={'A':0,'T':0,'G':0,'C':0} #reset the nt count to zero
	else:	
		nt_count['A']+=line.count('A') #count the values of each of the nts (remember to increment
		nt_count['T']+=line.count('T') 
		nt_count['G']+=line.count('G')
		nt_count['C']+=line.count('C')
	sequence_dict[gene_name]=nt_count #add the dicitonary to the dicitonary! 

print(sequence_dict)#print
