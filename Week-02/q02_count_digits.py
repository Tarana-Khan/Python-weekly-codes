n=int(input("enter number"))
count=0
while(n>0):
    r=n%10
    count+=1
    n=int(n/10);
print(count)
