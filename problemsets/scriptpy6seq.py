#!/usr/bin/env python3
answer=open("ans_python06seq","w")
with open("Python_06.seq.txt", "r") as file_read:
	#count=0 all theses count related and if else statments are true if the sequences in the original text file are in two lines  
	for line in file_read: #now the gene name and seq are sep by a tab
		line=line.rstrip()
		name,sequence=line.split('\t')#this splits the line into two strings instead of making a list. plus notice two variables!
		#count+=1
		#if count%2==0:
		answer.write(">"+name+"\n")
		Gc=sequence.replace('G','c')
		Cg=Gc.replace('C','g')
		At=Cg.replace('A','t')
		comp=At.replace('T','a')
		rev_comp=comp[::-1]
		rev_comp_uppercase=rev_comp.upper()
		answer.write(rev_comp_uppercase+ '\n')
		#else:
print("done")
answer.close()
file_read.close()
#print("rstriped") just to check what rstrip looks like
