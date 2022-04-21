# n is the target num, m is the laegest part of the sum digits
# how many combination to sum in increasing order
def count_partitions(n,m):
# decomposition: finding simpler instances of the problem
# explore two possibilities: use at least one 4; do not use 4
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m == 0:
		return 0
	else:
		with_m = count_partitions(n-m,m)
		without_m = count_partitions(n, m-1)
		return with_m + without_m
