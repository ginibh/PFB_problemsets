#!/usr/bin/env python3
numbers=[101,2,15,22,95,33,2,27,72,15,52]
numbers_it=iter(numbers)
for number in numbers_it:
	if number%2==0:
		print(number)

