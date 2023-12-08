def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1


p = 61
q = 53
n = p * q
nn = (p - 1) * (q - 1)

e = 17
d = pow(e, -1, nn)

pubkey = [e, n]
privkey = [d, n]
input_string = "burger"
ascii_message = [ord(char) for char in input_string]
print("asci message", ascii_message)

# encrypt
encrypted_message = [pow(letter, pubkey[0], pubkey[1]) for letter in ascii_message]

print("encr message", encrypted_message)

# decrypt

decrypt_message = [pow(letter, privkey[0], privkey[1]) for letter in encrypted_message]
print("decr message", decrypt_message)
