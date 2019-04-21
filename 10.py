'''Objective: Find the smallest positive number that is evenly divisible by all the numbers from 1-20'''

import math as m

def minPosNum():
	res = 1
	for i in range(1, 21):	#Iterates through the range 1-20
		x = (i // m.gcd(i, res)) #i floor divided by the greatest common divisor of i and res (which starts at 1)
		res *= x #result is multiplied by result * x
	return res	#returns solution at the end of for loop iteration

print(minPosNum())