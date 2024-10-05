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

def keygen():
    return 0

# p , q
# n = p * q
# r = (p-1)(q-1)
# e = 3, 5, 17, 65537 (can be others)
# d = e^-1 mod r
# public key: e,n
# private key: d
# LCM(a,b) = a*b / GCD(a,b)
# encryption: m^e mod(n)
# decryption: c^d mod(n)



print(mod_exp(76,11,5183))