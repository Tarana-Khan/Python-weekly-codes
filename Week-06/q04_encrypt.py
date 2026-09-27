main_str = input("Enter main string: ")
symbol = "@#"
encrypted = ""
for ch in main_str:
    encrypted += ch + symbol

print("Encrypted:", encrypted)
decrypted = ""
for i in range(0, len(encrypted), len(symbol)+1):
    decrypted += encrypted[i]

print("Decrypted:", decrypted)
