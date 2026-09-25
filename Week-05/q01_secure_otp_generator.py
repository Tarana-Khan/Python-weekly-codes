import math
import secrets
p = int(input("Enter first prime number: "))
while True:
    q = int(input("Enter second prime number: "))
    if p != q:
        break
    print("q must be different from p. Please enter a distinct prime.")
n = p * q
phi = (p - 1) * (q - 1)
e = None
for i in range(2, phi):
    if math.gcd(i, phi) == 1:
        e = i
        break

if e == None:
    raise ValueError("Could not find a valid 'e'. Ensure your prime numbers are valid.")

d = pow(e, -1, phi)

print("\n--- RSA Keys Generated ---")
print("Public Key: n=", n, " e=", e)
print("Private Key: n=", n, "d=",d)
max_otp_limit = min(900000, n - 100000)
if max_otp_limit <= 0:
    print(f"Warning: Your chosen primes yield an n ({n}) too small for standard 6-digit OTPs.")
    otp = secrets.randbelow(n)
    print("Original Generated OTP:",otp)
else:
    otp = secrets.randbelow(max_otp_limit) + 100000
    print("Original 6-Digit OTP:", otp)
encrypted_otp = pow(otp, e, n)
print("Encrypted OTP (Ciphertext):", encrypted_otp)
decrypted_otp = pow(encrypted_otp, d, n)
print("Decrypted OTP (Plaintext):", decrypted_otp)
