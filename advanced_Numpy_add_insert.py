"""
# insert = np.insert(array,index,value,axis=None)
with 2d axis 0 , row-wise
1 column wise
"""

import numpy as np

arr = np.array([10,20,30,40,50,60,70])
print("origional array")
print(arr)

new_arr = np.insert(arr,2,100,axis= 0)
print("new array")
print(new_arr)
print(len(new_arr))

# insert with 2d

print("insert with 2D array")
arr_2D = np.array([[2,3,4],[5,6,7]])
print("origional array")
print(arr_2D)
new_arr2D = np.insert(arr_2D,1,[10,50,60],axis = 0)  # if we axis = None they retrun flatted value
print("new 2D array")
print(new_arr2D)



# append   
"""
insert a value at the end of the array
"""
print("Append")
array = np.array([10,20,30,40,50,60,70,80,90,100])
print("origional arrat")
print(array)
print("append array")
new_array = np.append(array,[110,120,130,140,150,160,170,180,190,200])
print(new_array)


"""
concatenate : join 
np.concatenate((arr1,arr2), axis = 0)

axis 0 > vertical stacking
axis 1 > horizontal stacking
"""


arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
concatenated = np.concatenate((arr1,arr2))
print(arr1)
print(arr2)
print("concatenate")
print(concatenated)