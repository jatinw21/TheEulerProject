# https://www.hackerrank.com/contests/projecteuler/challenges/euler001

# Find the sum of all the multiples of 3 or 5 below N

def sum3n5(n):
  # it is rounded off automatically to floor
	numTermsOf3 = (n-1)/3
	numTermsOf5 = (n-1)/5
	numTermsOf15 = (n-1)/15

  #using formula for sum of first n numbers
	result = 3 * ((numTermsOf3) * (numTermsOf3 + 1))/2 \
		   + 5 * ((numTermsOf5) * (numTermsOf5 + 1))/2 \
		   - 15 * ((numTermsOf15) * (numTermsOf15 + 1))/2

	return result

# loop for test cases
t = int(raw_input())
i = 0;
while i < t:
	n = int(raw_input())
	answer = sum3n5(n)
	print answer
	i += 1
