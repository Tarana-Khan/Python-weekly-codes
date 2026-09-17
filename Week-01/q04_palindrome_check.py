n=int(input("enter number"))
rev=0
temp=n
while(n>0):
    r=n%10
    rev=rev*10+r;
    n=int(n/10);
if(rev==temp):
    print("given number is palindrome")
else:
    print("given number is not a palindrome")
