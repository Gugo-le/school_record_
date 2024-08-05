import random
from sympy import isprime, mod_inverse

def generate_large_prime(bitsize):
    """Generate a large prime number."""
    while True:
        num = random.getrandbits(bitsize)
        if isprime(num):
            return num

def generate_keypair(bitsize):
    """Generate RSA key pair (public key, private key)."""
    p = generate_large_prime(bitsize // 2)
    q = generate_large_prime(bitsize // 2)
    n = p * q

    phi = (p - 1) * (q - 1)

    # Choose e
    e = 65537  # A commonly used prime number for e

    # Calculate d
    d = mod_inverse(e, phi)

    return ((e, n), (d, n), (p, q))

def encrypt(public_key, plaintext):
    """Encrypt plaintext using the public key."""
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    """Decrypt ciphertext using the private key."""
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

def factorize_n(n):
    """Factorize n into p and q (basic trial division, not efficient for large n)."""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None

# RSA 키 생성
bitsize = 512
public_key, private_key, primes = generate_keypair(bitsize)

print("Public Key:", public_key)
print("Private Key:", private_key)
print("Primes p and q:", primes)

# 메시지 암호화 및 복호화
message = "Hello, RSA!"
print("Original message:", message)

encrypted_message = encrypt(public_key, message)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(private_key, encrypted_message)
print("Decrypted message:", decrypted_message)

# 소인수분해를 통해 개인 키 복원
e, n = public_key
p, q = factorize_n(n)
phi = (p - 1) * (q - 1)
d_reconstructed = mod_inverse(e, phi)
print("Reconstructed Private Key:", (d_reconstructed, n))

# 복원된 개인 키로 복호화
decrypted_message_with_reconstructed_key = decrypt((d_reconstructed, n), encrypted_message)
print("Decrypted message with reconstructed key:", decrypted_message_with_reconstructed_key)