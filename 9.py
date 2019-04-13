'''Objective: Find the largest prime factor of 600851475143'''

import math

n = 600851475143
maxFactor = []
for i in range(2, math.ceil(math.sqrt(n))): #From 2 -> square root of number
    while n % i == 0:   #Checks if numbers are divisible by anything else
        maxFactor.append(i) #If so, adds them to the list
        n /= i

print(maxFactor[-1])    #Ensures that only the max factor is returned, not other ones