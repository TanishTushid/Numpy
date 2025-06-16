"""
reshaping mean changing dimension of the array without 
modifying the data
#  arr.rshape(rows, columns)

reshaping is only possible if only dimension match
rezhaping doesnot create copy return view
"""

import pandas as np

arr = np.array([10,20,30,40,50,60])
print("origional array")
reshaped_arr = arr.reshape(2,3)
print("reshaping")
print(reshaped_arr)


"""
flattening array
1.ravel() -> return modification (view)
2.flatter() -> copy of origional array
used when you want to convert multi dimention array into 1D array

"""

arr_2d = np.array([[1,2,3],[4,5,6]])
print("convert into 1D array")
print(arr_2d.ravel())
#print(arr_2d.flatten())

