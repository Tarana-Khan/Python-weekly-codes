def merge_odd_even(list1,list2):
    result=[num for num in list1 if num%2!=0]+[num for num in list2 if num%2==0]
    return result
list1=[10,20,35,37,48]
list2=[55,71,61,70,80]
result=merge_odd_even(list1,list2)
print("merge list", result)
