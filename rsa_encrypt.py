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
            print("Prime number P:", p, file=sys.stderr)
            print("Prime number q:", q, file=sys.stderr)
            print("Public Key (e):", e, file=sys.stderr)
            print("Private Key:", d, file=sys.stderr)
            print("n:", n, file=sys.stderr)
            print("Phi of n:", phin, "", file=sys.stderr) #added a space after phi(n) to match the given log file
            return d
        tmp -= 1
    return 0

def get_nums(l):
    result = []
    for i in l.split():
        result.append(int(i))
    return result

def bchunks(i):
    result = []
    b = format(i, '064b')
    result.append(int(b[56:64], 2))
    result.append(int(b[48:56], 2))
    result.append(int(b[40:48], 2))
    result.append(int(b[32:40], 2))
    result.append(int(b[24:32], 2))    
    result.append(int(b[16:24], 2))
    result.append(int(b[8:16], 2))
    result.append(int(b[0:8], 2))
    return result
    
#separating input strings
lines = []
for line in sys.stdin:
    lines.append(line)
    
#get the public key from input
pub = get_nums(lines[1]) # or just line
e = pub[0]
n = pub[1]
d = dkey(e, n)

#printing the log to stderr and output to stdout
print("Message in ASCII code: [", end="", file=sys.stderr)
for i in range(0, len(lines[0])-2):
    print(ord(lines[0][i]), end=", ", file=sys.stderr)
print(ord(lines[0][len(lines[0])-2]), end="", file=sys.stderr)
print("]", file=sys.stderr)

print("\nMessage encoded [", end="", file=sys.stderr)
for i in range(0, len(lines[0])-2):
    #output to stderr for log
    c = encrypt(ord(lines[0][i]), e, n)
    print(c, end=", ", file=sys.stderr)
    #splitting into byte chunks for padding
    chunks = bchunks(c)
    for t in chunks:
        #encoded to latin1 to match the binary of test case output
        sys.stdout.buffer.write(chr(t).encode('latin1')) #stdout option
#last character is treated differently due to log output
c = encrypt(ord(lines[0][len(lines[0])-2]), e, n)
print(c, end="", file=sys.stderr)
print("]", file=sys.stderr)
#Last character to latin1 to match the test case output
chunks = bchunks(c)
for t in chunks:
    sys.stdout.buffer.write(chr(t).encode('latin1')) #stdout option
    