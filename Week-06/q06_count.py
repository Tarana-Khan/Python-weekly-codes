s = input("Enter a string: ")
upper = lower = alpha = digit = 0
for ch in s:
    if ch.isupper():
        upper += 1
    if ch.islower():
        lower += 1
    if ch.isalpha():
        alpha += 1
    if ch.isdigit():
        digit += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Total Alphabets:", alpha)
print("Digits:", digit)
