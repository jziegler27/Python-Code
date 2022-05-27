# Simple program that estimates value of pi using simulated dart board. 
import random
import math

darts = int(input("number of darts to throw: "))
hit = 0
for dart in range(darts):
    x = random.random()
    y = random.random()
    if math.sqrt(x*x + y*y) < 1:
        hit += 1
pi_estimate = 4*(hit/darts)
print(f"pi estimate = {pi_estimate}")