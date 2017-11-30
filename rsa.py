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

#generate public and private keys
def gen_keys():
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

    #get phi(n)
    t = (p -1) * (q-1)
    
    #find e such that e and t are coprime gcd(e,t) == 1
    for i in range(2, t):
        if gcd(i, t) == 1:
            e = i
            break
    
    for i in range(2, t):

        if i * e % t == 1:
            d = i
            break
    return  e, n, d


#encrypts text
def encrypt(e, n):
    pt = list(input("\nenter plain text to encrypt: "))
    pt = [ ord(x) for x in pt]
    print("\n##########################")
    print("Pre encryption")
    print(pt)

    ct = []
    #encrypt each element
    for el in pt:
        ct.append( (pow(el, e) % n))
    print("Post encryption")
    print(ct)
    print("##########################")
    return ct

def decrypt(ct, d, n):
    #decrypt each element
    pt = []
    for el in ct:
        pt.append(chr((pow(el, d) % n)))
    #print("the decrypted message is: " + str(ct))
    print("\n##########################")
    print("The Decrypted message is:")
    print(''.join(pt))
    print("##########################")

def main():

    #generate public and private keys 
    e, n, d = gen_keys()
    
    choice = -1

    while choice is not "0":

        print('\n-------------------')
        print("RSA Program")
        print("encrypt: press 1")
        print("decrypt: press 2")
        print("exit: press 0")
        print('-------------------\n')

        choice = input("Choose option: ")


        #encrypt message
        if choice == "1":
            ct = encrypt(e, n)
            print(len(ct))

        #decrypt the message pt
        if(choice == "2"):
            try:
                decrypt(ct, d, n)
            except (UnboundLocalError,TypeError):
                print("no encrypted text found, select option 1 to encrypt")

if __name__ == "__main__":
    main()