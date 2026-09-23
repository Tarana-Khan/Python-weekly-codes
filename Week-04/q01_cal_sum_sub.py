def cal_sum_sub(a,b):
    add=a+b;
    sub=a-b;
    return add,sub;
n1=int(input("enter first no."))
n2=int(input("enter second no."))
addRes,subRes=cal_sum_sub(n1,n2)
print("Addition:",addRes, "Subtraction:", subRes)
