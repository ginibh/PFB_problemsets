#!/usr/bin/env python3
import Bio
from Bio import SeqIO
from Bio.Seq import Seq
sizes=[len(record) for record in SeqIO.parse("Python_08.fasta","fasta")]
total_num_sequences=len(sizes)
min_seq_size=min(sizes)
max_seq_size=max(sizes)
print('Total:',total_num_sequences,'min:',min_seq_size,'max:',max_seq_size)












#records=list(SeqIO.parse("Python_08.fasta","fasta"))
#num_records=len(records)
#print("Total reads:",num_records)
#for seq_record in SeqIO.parse("Python_08.fasta","fasta"):
#	length_of_records=len(str(seq_record.seq))
#	print("Length of each record is:",length_of_records)




	
