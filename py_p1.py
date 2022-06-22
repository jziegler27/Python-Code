import random, sys, math
darts = int(sys.argv[1])
hit = 0
for dart in range(darts):
        x = random.random()
        y = random.random()
        if math.sqrt(x*x + y*y) < 1:
            hit += 1
pi_estimate = 4*(hit/darts)
print(f"pi estimate = {pi_estimate}")

