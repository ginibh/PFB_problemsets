#!/usr/bin/env python3
humans='sapiens, erectus, neanderthalensis'
print(humans)
human=humans.split(',')
print(human)
human_alpha=sorted(human,key=None,reverse=False)
print(human_alpha)
length=[]
for values in human_alpha:
	length.append(len(values))
print(length)
length_sorted=sorted(length,reverse=False)
print(length_sorted)
