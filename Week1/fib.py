def fib(x):
	total = 0

	if(x == 0 or x == 1):
		return 1;
	else:
		old = 1
		older = 1

		for i in xrange(1,x):
			total = old + older 
			older = old
			old = total
	
	return total

print fib(150)		
