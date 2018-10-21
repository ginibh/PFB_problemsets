#!/usr/bin/env python3
class seqCharacteristics(object):#create a class
	def __init__(self,sequence,seq_name,species_name):#this gives the attributes to your class
		self.sequence=sequence#notice the use of self. this needs to be consistent and is formulaic
		self.seq_name=seq_name
		self.species_name=species_name
	def len_sequence(self):
		length=len(self.sequence)#self. sequence keep referring to self
		return length
	def nucleotidecomp(self):
		countA=self.sequence.count('A')
		countG=self.sequence.count('G')
		countC=self.sequence.count('C')
		countT=self.sequence.count('T')
		nucleotide_comp=('A:',countA,'G:',countG, 'C:',countC,'T:',countT)
		return nucleotide_comp
	def GCcontent(self):
		countG=self.sequence.count('G')
		countC=self.sequence.count('C')
		length=len(self.sequence)
		GC_content=(countG+countC)/length
		GC_content_percentage='{:.2%}'.format(GC_content)
		return GC_content_percentage
	def Fastaformat(self):#remember the print formating and use that to take a sequence and print in fasta format
		fasta=">{}\n{}".format(self.seq_name,self.sequence)
		return fasta
 
char_1=seqCharacteristics('ATGCTAGCTACGTAGCTAGCA','rb1','My fiction')#these define your object
char_2=seqCharacterisitcs('ATGCTAGCTACGTAGCTAGCA','rb1','My fiction')
for char in [char_1,char_2]:
	print('Name of sequence:',char.seq_name,'','Name of species:',char.species_name)#notice char.something this is really important for the code to work and is referring to the things in char_1
	print('Sequence length:',char.len_sequence())
	print('Nucleotide composition:',char.nucleotidecomp())
	print('GC content is:',char.GCcontent())
	print(char.Fastaformat())
