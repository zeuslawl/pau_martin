#coding:utf-8

for fil in xrange(1,7,1):
	for col in xrange(1,6,1):
		if (fil == 1 and col == 3):
			print "*",
			
		else:
			if (fil == 2 and col == 3):
				print "A",
			else:
				if (fil == 3 and (col == 2 or col == 3 or col == 4)):
					print "A",
				else: 
					if (fil == 4):
						print "A",
					else: 
						if ((fil == 5 and col == 3) or (fil == 6 and col == 3)):
							print "N",
						else: 
							print " ",
	print ""
		
		
