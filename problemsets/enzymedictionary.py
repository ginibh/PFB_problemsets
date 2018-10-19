#!/usr/bin/env python3
import re
enzyme_list=open("bionet.txt","r")
enzyme_dict={}
enzyme_name=""
recognition_site=""
for line in enzyme_list:
	line=line.rstrip()
	if not line.startswith("#"):#headerlines were given # so the script can ignore it 
		#print(line)this allows to check that file has no header
		for match in re.finditer(r"(.+.\S\W)\s{4,}(.+)",line):#use regex101 ot fiddle with regular expressions and the s{4,} gets rid of white space between columns
			enzyme_name=match.group(1) #1st set of ()
			recognition_site=match.group(2) #2nd set of ()
			enzyme_dict[enzyme_name]=recognition_site #add to dictionary
			print(enzyme_dict) #print
print("All done")	
