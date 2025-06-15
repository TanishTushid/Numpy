
"""
by the help of indexing and slicing we can 
access specific position, element of array
indexing : select single element in the array
slicing : slect multiple elemnt in the array
"""
#acces specific element 
"""
array[index] #1d array
array[row,column]  #2d array
"""

import numpy as np

arr = np.array([10,20,30,40,50])
print("origional array")
print(arr)
print("first element")
print(arr[0])
print("third element")
print(arr[2])
print("last element")
print(arr[-1])

"""slicing mean extracting subset of data
   arr[start:stop:step]
"""

array = np.array([10,20,30,40,50,60,70,80,90,100])
print("origional array")
print(array)
print("value 1 to 4")
print(array[0:5])
print("value 1 to end by step 2")
print(array[::2])
print("reverse")
print(array[::-1])

""" fancy indexing select multiple element at once   its used more with non-sequencial"""
print("multi with fancy")
print(array[[0,2,4,8]])


""" boolean maskeing another name filtering. filter data with condition"""
print("greather than 25")
print(array[array>50])
