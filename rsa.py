import sys

debug = 0

def gcd(a, b):
    while(b != 0):
        c = b
        b = a%b
        a = c
    return a

def mod_exp(b, e, m):
    result = 1
    if m==1:
        return 0
    for i in range(e):
        result = (result * b) % m
        if(debug):
            print("result: %i\n", result)
    return result

def encrypt(m, e, n):
    return mod_exp(m, e, n)

def decrypt(c, d, n):
    return mod_exp(c, d, n)

def dkey(e, n):
    p = 0
    q = 0
    # factorize n by testing from square root
    tmp = n ** (1/2)
    # round tmp to whole number
    tmp = int(tmp)
    while(tmp > 0):
        if(n % tmp == 0):
            p = tmp
            q = int(n/tmp)
            if(debug):
                print("p: ", p, " q: ", q)
            # phi function: (p-1)(q-1)
            phin = int((p-1)*(q-1))
            if(debug):
                print("phi(n): ", phin)
            # d = e^-1 mod phi(n)
            d = pow(e, -1, phin)
            return d
        tmp -= 1
    return 0


# p , q
# n = p * q
# phi(n) = (p-1)(q-1)
# e = 3, 5, 17, 65537 (can be others)
# d = e^-1 mod phi(n)
# public key: e,n
# private key: d
# LCM(a,b) = a*b / GCD(a,b)
# encryption: m^e mod(n)
# decryption: c^d mod(n)


#for line in sys.stdin:
#    line = line.strip()
#    print(line)

