list=[]
print("enter 20 number");
for i in range(1,21):
    n=int(input(i));
    list.append(n);
for i in list:
    if(i%5==0):
        print(i);
