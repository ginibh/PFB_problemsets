#!/usr/bin/env python3
import Bio
import sys
from Bio import SeqIO
file_name=sys.argv[1]
length_kmer=int(sys.argv[2])
num_top_kmers=int(sys.argv[3])
fastq_records=SeqIO.parse(file_name,"fastq")
kmer_dict={}
for line in fastq_records:
#	line=line.rstrip()
	sequence=str(line.seq)
	for position in range(0,(len(sequence)-length_kmer)):#this is important because you don't want the remainder of the lines. so you substract the length_kmer
		kmer=sequence[position:position+length_kmer]#kmer is a position +the length of the kmer
		if not kmer in kmer_dict:
			kmer_dict[kmer]=1#if it is a new kmer then the value is one
		else:
			kmer_dict[kmer]+=1 #otherwise an already identified kmer should increase its value by 1 
kmer_dict_sorted=sorted(kmer_dict.items(),key=lambda x:x[1],reverse=True) #now that we have a dict, we need to sort it. this sorting function makes it into a list of tupules
#print(kmer_dict_sorted) #you can print the list if you want to check
counter=1 #set the counter to 1 not zero because you want it to print top 10
for kmer,value in kmer_dict_sorted: #since each tupule has a key and a value
	print(kmer, '\t',value)	#print the kmer tab value
	counter+=1 #increase the counter by 1
	if counter>num_top_kmers: #if this exceeds the top few you need
		break #stop the code
	
