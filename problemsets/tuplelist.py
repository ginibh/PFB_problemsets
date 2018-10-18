#!/usr/bin/env python3
sequences=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
sequences_iter=iter(sequences) #iterate the sequence to create individual sequences
#lengths=[]	#create a list of lengths of the seq in sequences
#for seq in sequences:
#	lengths.append(len(seq))
seq_and_len=[(len(x),x) for x in sequences]
print(seq_and_len)


