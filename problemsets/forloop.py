#!/usr/bin/env python3
sequences=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
sequences_iter=iter(sequences)
for seq in sequences_iter:
	print(len(seq), '\t', seq)

		
