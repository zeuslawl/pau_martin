#!/usr/bin/python
# coding: utf8

for fil in xrange(1,6,1):
	print ""
	for col in xrange(1,5,1):
		if fil == 1:
			if col ==2:
				print "A",
				
			else:
				if col ==3:
					print "B",
				else:
					if col==4:
						print "C",
					else:
						print "-",
		
		if col==1: 
			if not(fil == 1):
				print fil -1,
				
		if fil == 2:
			if not(col==1):
				print "-",
		
		if fil==3:
			if not(col==1 or col==3):
				print "-",
			else:
				if col==3:
					print "*",
		
		if fil ==4:
			if not(col==1 or col==2):
				print "-",
			else:
				if col==2:
					print "*",
		if fil==5:
			if not(col==1):
				print "-",
