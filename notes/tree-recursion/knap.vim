# if the digits in n could sum up to k
def knap(n, k):
	if n == 0:
		return k == 0

	with_last = knap(n//10, (k-n)%10)
	without_last = knap(n//10, k)
	return with_last or without_last
