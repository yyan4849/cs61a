def split(n):

	return n//10, n%10

#recursive call
def sum_digits(n):
	#test for the base case
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return sum_digits(all_but_last) + last

def sum_digits_iter(n):
	digit_sum = 0
	while n > 0:
		n, last = split(n)
		digit_sum = digit_sum + last
	return digit_sum

def luhn_sum(n):
#if n is smaller than 10, that is to say only one digit so just return
	if n < 10:
		return n
	else:
#more than one, return all_but_last plus the last digit
		all_but_last, last = split(n)
		return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
# break up n->all_but_last
	all_but_last, last = split(n)
# every second digit 
	luhn_digit = sum_digits(2*last)
# if only one digit return
	if n < 10:
		return luhn_digit
	else:
		return luhn_sum(all_but_last) + luhn_digit
