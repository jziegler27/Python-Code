def primes(low, high):
    for number in range(low, high + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                yield number


import sys
for prime in primes(int(sys.argv[1]),int(sys.argv[2])):
    print(prime)
