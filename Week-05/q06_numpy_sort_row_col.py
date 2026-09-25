import numpy as np
arr=np.array([[3,6,9,12],[15,35,11,24],[27,5,33,36],[39,42,72,48],[51,83,57,60]])
print("original Array", arr)
sorted_by_row=arr[:,arr[1,:].argsort()]
print("sorted by second row",sorted_by_row)
sorted_by_col=arr[arr[:,1].argsort()]
print("sorted by second column",sorted_by_col)
