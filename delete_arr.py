"""
1D-Array
remoce at the specific index and return new array, old array are same
np.delete(array,index,axis =None)
axis None mean we delete from flattern array 
"""

import numpy as np

arr = np.array([10,20,30,40,50,60])
print("array")
print(arr)
new_arr = np.delete(arr,1,axis = None)
print("delete element 2")
print(new_arr)

"""
2D-Array
0-> row
1-> column
"""

new_arr = np.array([[10,20,30],[40,50,60]])
print("2D-Array")
print(new_arr)
arr_del = np.delete(new_arr,0, axis=0)
print("delete 1 row")
print(arr_del)

