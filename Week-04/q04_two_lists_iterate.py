def reverse(nums1,nums2):
    for i,j in zip(nums1,nums2[::-1]):
        print(i,j)
l1=[10,20,30,40,50]
l2=[10,20,30,40,50]
reverse(l1,l2)
