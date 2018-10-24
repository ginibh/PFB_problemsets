#!/usr/bin/env python3
import Bio
from Bio import SeqIO
import re
file_open=open("bowtie2.sam","r")#open a sam file
rna_dict={} #need to create a dictionary
for line in file_open:
	y=line.split('\t')#split lines on tabs, this will return a list
	gene_name=y[2].split('^')[0]#split the name at this sign to get only the first part of the gene add [0]
	read_name=y[0]	#this is the read name. position 0 in the list is the transcript read name
	if gene_name in rna_dict:
		rna_dict[gene_name].add(read_name) #if gene_name already exists, then add the read name to the set
	else:
		rna_dict[gene_name]=set() #if it is a new gene then create a set
		rna_dict[gene_name].add(read_name) #and after creating the set, add the read_name
dict_transcripts_per_gene={} #create a new dictionary
for gene_name in rna_dict:
	dict_transcripts_per_gene[gene_name]=''#add gene names to the key
	sum_transcripts=len(rna_dict[gene_name]) #len of the set created in the previous for loop. since we don't have a name of the value, enter the dict name with the ket=y. len will give you number of items in set
	dict_transcripts_per_gene[gene_name]=sum_transcripts #append the dictionary
#print(dict_transcripts_per_gene)
dict_transcripts_per_gene_sorted=sorted(dict_transcripts_per_gene.items(),key=lambda x:x[1],reverse=True)#sort from highest to lowest. this returns a list
#print(dict_transcripts_per_gene_sorted)
for gene,value in dict_transcripts_per_gene_sorted:#print the key and value in columns
	print(gene,'\t',value)#print the columns

	
print(dict_transcripts_per_gene)

