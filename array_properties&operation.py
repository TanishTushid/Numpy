"""
how to check size,shape,type?
1 find structure, no of dimension
"""
#checking

#shape  basically kitni rows,colomns hai, use when work with 
#multi-dimension data 

import numpy as np 
arr_2d = np.array([[1,2,3],[4,5,6]])
print("array")
print(arr_2d)

#shape shape of array
print("shape of array")
print(arr_2d.shape)

#size check total no of element in array
print("size of array")
print(arr_2d.size)

#ndim mean number of dimension  
print("dimension of array")
arr_1d = np.array([1,2,3,4,5,6])
arr_2_d = np.array([[1,2,3],[4,5,6]])
arr_3d = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print('1-D')
print(arr_1d.ndim)
print('2-D')
print(arr_2_d.ndim)
print('3-D')
print(arr_3d.ndim)

#dtype  type of element
arr = np.array([10,20,25.5,30.8,40])
print("Datatype")
print(arr.dtype)


#conversion

array = np.array([2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5])
print(array)
print(array.dtype)
print("convert into int")
arr_int = array.astype(int)
print(arr_int)
print(arr_int.dtype)
