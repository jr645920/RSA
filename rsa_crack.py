import sys

debug = 0

def mod_exp(b, e, m):
    result = 1
    if m==1:
        return 0
    for i in range(e):
        result = (result * b) % m
        if(debug):
            print("result: ", result)
    return result

# encryption: m^e mod(n)
def encrypt(m, e, n):
    return mod_exp(m, e, n)

# decryption: c^d mod(n)
def decrypt(c, d, n):
    return mod_exp(c, d, n)

# private key: d
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
            # phi function: (p-1)(q-1)
            phin = int((p-1)*(q-1))
            if(debug):
                print("phi(n): ", phin)
            # d = e^-1 mod phi(n)
            d = pow(e, -1, phin)
            #stderr for log
            print("Prime numbers: ", p, ", ", q, sep='')
            print("Private key:", d)
            return d
        tmp -= 1
    return 0

def get_nums(l):
    result = []
    for i in l.split():
        result.append(int(i))
    return result

def bchunks(i):
    result = ''
    result += i[56:64]
    result += i[48:56]
    result += i[40:48]
    result += i[32:40]
    result += i[24:32]    
    result += i[16:24]
    result += i[8:16]
    result += i[0:8]
    return result
    
#separating input strings
lines = []
for line in sys.stdin.buffer:
    line = line.decode('latin1')
    lines.append(line)

# for i in range(0, len(lines)):
#     sys.stdout.buffer.write(lines[i].encode('latin1'))

ciphertext = ''
for i in range(0, len(lines)-1):
    ciphertext += lines[i]

#divide ciphertext into chunks
tmp = ''
for i in range(0, len(ciphertext)):
    tmp += format(ord(ciphertext[i]), '08b')
ciphertext = tmp
plaintext = []
j = 0
for i in range(64, len(ciphertext), 64):
    chunk = ciphertext[j:i]
    plaintext.append(int(bchunks(chunk), 2))
    j += 64

#get the public key from input
pub = get_nums(line)
e = pub[0]
n = pub[1]
d = dkey(e, n)

print("Unencrypted message:")
for i in range(0, len(plaintext)):
    m = decrypt(plaintext[i], d, n)
    print(chr(m), end='')

print('') #for test case formatting