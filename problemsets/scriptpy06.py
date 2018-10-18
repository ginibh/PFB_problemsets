#!/usr/bin/env python3
fo=open("anstopy06.txt","w") #create a file to write into
with open ("Python_06.txt", "r") as file_read:#open the file to read
	for line in file_read: #for loop for each line in the file
		line_upper=line.upper() #convert to upper case
		fo.write(line_upper) #print every line to the file 
	 # 	print(line_upper) #this will print to std output i.e. screen
print("done converting to upper case!") #to let user know you're done
file_read.close() #close read file 
fo.close() #close write file
