#!/usr/bin/env python3
import Bio
from Bio import SeqIO
record_dict={}
for record in SeqIO.parse("ecoliPB-filtered_0.50.contigs.fasta","fasta"):
	seq_ID=record.id#parse the record for ID
	sequence=record.seq #parse the record for sequence
	record_dict[seq_ID]=sequence#create a dictionary	
#print(record_dict)
Total_number_of_records=len(record_dict) #getting the total number of keys in a dictionary
print(Total_number_of_records)
len_Seq_list=[]#create a list of lengths of sequences
for record in SeqIO.parse("ecoliPB-filtered_0.50.contigs.fasta","fasta"):
	sequence=record.seq#define the sequence
	len_seq=len(sequence)#determine the length of sequence
	len_Seq_list.append(len_seq) #create a list with lengths
print(len_Seq_list) #print the list
Shortest_contig=min(len_Seq_list)#the shortest contig is the smallest element in the list
Longest_contig=max(len_Seq_list)#the longest is the largest element in the list
print('The shortest conting is:',Shortest_contig,'The longest contig is:',Longest_contig)
#for contig in len_Seq_list:
genome_length=sum(len_Seq_list)#the sum of the lengths of all the sequences is the size of the genome
half_genome_length=genome_length/2 #the half genome length
len_Seq_list_sorted=sorted(len_Seq_list,reverse=True) #sort based on size. this sorts largest to smallest which is what you want for this analysis
print(len_Seq_list_sorted)
count=0 #for calculating n50
for i in range(len(len_Seq_list_sorted)):#use the range function
	count+=len_Seq_list_sorted[i]#remember i is the index so you need to call on it
	if count>=half_genome_length: 
		N50=len_Seq_list_sorted[i]#to get the position which exceeded the half the length of the genome. N50 is the value which assembles just before the half length of the genome. 
		print("N50 value is:",N50)#print value
		break #break is used to stop after the condition is met
list_for_L50=[i for i in len_Seq_list_sorted if i>N50] #you want to create a list which has values of every position i in list if i is greater than N50
print("L50 value is:",len(list_for_L50)) #print the len of the list because this will give you the number of elements left. L50 is the number of contigs greater than N50 value. 


