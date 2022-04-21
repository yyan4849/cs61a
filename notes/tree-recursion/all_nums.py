# use 0,1 to combine nums no more than n
def all_nums(k):
	def h(k, prefix):
		if k == 0:
			print(prefix)
			return 
		h(k-1, prefix * 10)
		h(k-1, prefix * 10 +1）
