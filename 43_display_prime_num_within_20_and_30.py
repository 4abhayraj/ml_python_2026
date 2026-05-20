def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

primes=[]
for n in range (20,30):
    if is_prime(n):
        primes.append(n)
print(primes)

