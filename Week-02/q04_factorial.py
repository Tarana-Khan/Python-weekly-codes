factorial=lambda n:1 if n<=1 else n*factorial(n-1)
n=int(input("enter number"))
print(factorial(n))
