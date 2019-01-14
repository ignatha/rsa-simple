for i in xrange(100000,100099):
	count = 0
	for x in xrange(1,i+1):
		if i%x == 0:
			count += 1

	if count == 2:
		print(i)