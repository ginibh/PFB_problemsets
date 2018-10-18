#!/usr/bin/env python3
ragini_fav_things={}
ragini_fav_things['song']='crazy_train'
ragini_fav_things['book']='sapiens'
ragini_fav_things['tree']='pine'
print(ragini_fav_things) #printing the dictionary
print(ragini_fav_things['book'])#printing the value to book
fav_thing='book' #assigning a variable to book and then printing the variable
print(ragini_fav_things[fav_thing])
print(ragini_fav_things['tree'])
fav_tree='tree'
print(ragini_fav_things[fav_tree])
ragini_fav_things['organism']='tiger' #add organism to dictionary 
fav_thing='organism'
print(ragini_fav_things[fav_thing])
print(ragini_fav_things)
#for key in ragini_fav_things:
#	print(key) #this will print the list of keys
#user_ques=input('which of these do you like?') #this is how to ask the user a question using raw_input()
#user_ans=input('give me an example')
#ragini_fav_things[user_ques]=user_ans
#print(ragini_fav_things)
for key in ragini_fav_things: #a for loop to get all keys and values
	value=ragini_fav_things[key]
	print(key, value)
