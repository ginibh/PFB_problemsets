#!/usr/bin/env python3
import re #import re
import sys #import sys
file_open_1=open("/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/spr/starAlignerWorkshop/Log.final.out","r")#open file
unmapped_reads=[] #create a list to capture all unmapped reads (3 categories)
for line in file_open_1: #start the for loop going line by line
	line=line.rstrip() #strip line of extra space at end
	for value in re.findall(r"Uniquely mapped reads number\s[|]\s(.*)", line):#write regex for uniquely mapped reads
		print("Uniquely mapped reads number:", '\t', value)
	for value in re.findall(r"Mismatch rate per base\,\s\%\s\|\t(.*)",line):#write regex for mismatch rate
		print("Mismatch rate per base:", '\t', value)
	for value in re.findall(r"\% of reads unmapped:\s+.*\|\t(.*)%",line):#for all unmapped reads statements
		unmapped_reads.append(float(value))#append the list with the values. they are strings so make sure to use float to only keep the decimal values
print(unmapped_reads) #check the list of values with unmapped reads 
Total_unmapped_reads=sum(unmapped_reads) #sum of all the values in the list 
print(Total_unmapped_reads) #get the total unmapped reads values
	
			



