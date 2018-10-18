#!/usr/bin/env python3
f_write=open("fastqans.txt","w") #open file to write
with open("Python_06.fastq","r") as f_read: #open read file
	line_count=0 #two variables are getting counted
	length=0
	for line in f_read:
		line=line.rstrip()
		line_count +=1 #for every line the count goes up by one
		length+=len(line) #for every line it add length of line
	f_write.write("Total no of characters:"+str(length)+ "\n"+"Total line count:"+str(line_count)+"\n") #write to file length and characters
Avg_line_length=length/line_count #cal avg line length
f_write.write("The average line length is:"+str(Avg_line_length)+'\n')#write average line length
print("Done") #tell user that you're done writing the file
f_write.close() #close read and write files
f_read.close()
