"""
collention of number. collection of value which is store to together
in the organised way called array

"""
"""
1D- ARRAY
list of number which is store in single one line
"""

import numpy as np 
array_1D = np.array([10,20,30,40,50])
print("1-D Array")
print(array_1D)


"""
2-D array  its like a table which have rows and columns 
"""
array_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2-D array")
print(array_2D)

"""
Multi-D array  mean array which have multiple dimention use in AI,Deep learning, MR scan
"""
#matrix

matrix = np.array([[1,2,3],[4,5,6]])
print("matrix")
print(matrix)


#creating arrays from python list
"""
np.array([[ele1],[ele2],[ele3]])
"""
"""
array with default value's
"""
zerroes_array = np.zeros(3)
print("zerroes_array_1D")
print(zerroes_array)

zerroes_array_2D = np.zeros((3,3))
print("zerroes_array_2D")
print(zerroes_array_2D)

"""
fill's with 1
"""
one_array = np.ones(8)
print("one filled array")
print(one_array)

print("multi-dimention")
print(np.ones((5,5)))

"""
full function , when use , when we have specific number with starting
"""
print("specific value")
print(np.full((2,2),7))

