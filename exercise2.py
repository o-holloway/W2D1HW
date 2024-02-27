#Get first prime numbers up to 100

def primes_to_100():
    for n in range(2,100):
        q = True
        for x in range(2,n):
            if n % x == 0:
                q = False
                break
        if q == True:
            print(f"{n} is prime")

primes_to_100()