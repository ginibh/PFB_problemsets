#!/usr/bin/env python3
sequences=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
sequences_iter=iter(sequences)
count=0
for seq in sequences_iter:
	print(count, len(seq), '\t',seq)
	count+=1
#print(len(seq), '\t', seq)

