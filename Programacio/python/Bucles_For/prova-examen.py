#!/usr/bin/python
# coding: utf8

for fil in xrange(1,11):
	print ""
	for col in xrange(1,11):
		if fil == 1:
			if not col == 1:
				print col -1,
			
			else:
				print "-",
		
		else: 
			if col == 1:
				print fil - 1,
				
			else: 
				if fil == 5 and col == 3:
					print "*",
				
				elif fil == 3 and col == 9:
					print "*",
					
				else:
					print "-",
