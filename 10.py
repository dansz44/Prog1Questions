'''Objective: Find the smallest positive number that is evenly divisible by all the numbers from 1-20'''

import math as m

def minPosNum():
	res = 1
	for i in range(1, 21):
		res *= (i // m.gcd(i, res))
	return res

print(minPosNum())