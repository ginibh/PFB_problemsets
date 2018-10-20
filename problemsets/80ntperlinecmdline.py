#!/usr/bin/env python3 
import sys
fasta_filename=sys.argv[1] #get a file
fasta_fileobject=open(fasta_filename,'r')#open file
out_file=sys.stdout #this is another way to print
limit_1=int(sys.argv[2]) #make sure the int fn is added since this is a number =80
def align80(dna,limit):
	#dna_strip=dna.strip()
	#dna_new=dna_strip.replace('\n','')#this will replace empty lines with nothing	
	#dna_sub="i" #creates an empty folder
        #pattern = r'\w{1,' + limit_1 + r'}'this is max's way. ignore for now
        #re.findall(pattern, dna)
	dna_sub='' #create an empty variable
	for position in range(0,len(dna),limit):#creates a range with positions
		#print(position)
		dna_sub=dna_sub+dna[position:position+limit]+'\n'#you need to add it to sub_dna and the range needs to keep adding 80	
	#print(dna_sub)
	return dna_sub
seq_name=''#create an empty variable for name
seq_desc=''#---''---for desc
seq_string=''#---"-- for string
for line in fasta_fileobject: #make it start reading the file
	line=line.rstrip() #strip empty space from the right side
	if line.startswith('>'):
		if len(seq_string)>0:#this is when you have a sstring
			seq_align_80=align80(seq_string,limit_1) #call a function defined earlier
			print(">{} {}\n{}".format(seq_name,seq_desc,seq_align_80)) #print
			seq_string=''#create a new string to fill
		line=line.lstrip('>') #lstrip strips from left so removes >
		seq_name,seq_desc=line.split(maxsplit=1) #this splits at exactly one space
	else:
		seq_string+=line #get line
if len(seq_string)>0:#for the last string that doesn't have another line below it 
	seq_align_80=align80(seq_string,limit_1) #call function
	print(">{} {}\n{}".format(seq_name,seq_desc,seq_align_80)) #print
