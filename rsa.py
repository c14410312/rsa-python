import random 
from fractions import gcd

'''
RSA implementation in python security lab 4
Dylan Butler 30/11/17
'''

_test_iter = 5 # used for miller rabin algorithm

#function to check if num prime using miller-rabin method
def is_prime(n):
    
    if n == 2:
        return True

    #n needs to be odd
    if n % 2 == 0:
        return False
    
    s = 0
    d = n - 1


    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(_test_iter):
        a = random.randrange(2, n-1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False #n is composite
    return True # n is prime

def main():
    
    #loop until both p and q are prime
    while True:
        
        #p =random.randint(0, 1000)
        #q = random.randint(0, 1000)

        p = 11
        q = 17

        if (is_prime(p) and is_prime(q)):
            break
    #get the mod
    n = p * q
    print("mod = " + str(n))

    #get phi(n)
    t = (p -1) * (q-1)
    print("phi(n) = " + str(t))
    #find e such that e and t are coprime gcd(e,t) == 1
    for i in range(2, t):
        if gcd(i, t) == 1:
            e = i
            break
    print("e = " + str(e))
    for i in range(2, t):

        if i * 7 % t == 1:
            d = i
            break
    print("d=" + str(d))
if __name__ == "__main__":
    main()