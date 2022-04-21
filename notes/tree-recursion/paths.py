from ucb import trace
@trace

def paths(m,n):
	if m == 1 or n == 1:
		return 1
	return paths(m-1, n) + paths(m, n-1)
