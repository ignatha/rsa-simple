# GCD operator
def computeGCD(a,b):
	if(b==0):
		return a
	else:
		return computeGCD(b,a%b)