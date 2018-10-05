#coding:utf-8

for fil in xrange(1,9,1):
	for col in xrange(1,9,1):
		if (fil == 1 or fil == 3 or fil == 5 or fil == 7):
			if (col % 2 == 0):
				print "B",
			else: 
				print "N",
				
		else:
			if (col % 2 == 0):
				print "N",
			else: 
				print "B",
	print ""
