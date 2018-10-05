#coding:utf-8

for fil in xrange(1,5,1):
	for col in xrange(1,9,1):
		if ( fil == 1):
			print "*",
		
		else: 
			if ( fil == 2):
				if (col == 1 or col == 8):
					print "*",
				else: 
					if (col == 4):
						print ":",
					else:
						if (col == 5):
							print ")",
						else: 
							print " ",
			else:
				if (fil == 3):
					if (col == 1 or col == 8):
						print "*", 
					else: 
						if (col == 4):
							print ":",
						else: 
							if (col == 5):
								print "(",
							else: 
								print " ",
				else: 
					print "*", 
	print ""
