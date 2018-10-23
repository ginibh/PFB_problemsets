#!/usr/bin/env python3
import Bio
from Bio import SeqIO
record_dict={}
for record in SeqIO.parse("ecoliPB-filtered_0.50.contigs.fasta","fasta"):
	seq_ID=record.id
	sequence=record.seq
	record_dict[seq_ID]=sequence	
#print(record_dict)
Total_number_of_records=len(record_dict) #getting the total number of keys in a dictionary
print(Total_number_of_records)
len_Seq_list=[]
for record in SeqIO.parse("ecoliPB-filtered_0.50.contigs.fasta","fasta"):
	sequence=record.seq
	len_seq=len(sequence)
	len_Seq_list.append(len_seq)
print(len_Seq_list)
Shortest_contig=min(len_Seq_list)
Longest_contig=max(len_Seq_list)
print(Shortest_contig,Longest_contig)	
