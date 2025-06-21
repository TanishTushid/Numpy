"""
vectorization -> mean apply a operation on entire array without using
the loop's.
very fast
"""

# example by using of loop
# work with large list its go slow
list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]

result = [x + y for x,y in zip(list_1,list_2)]
print("by the using of loop's")
print(result)


import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr_1 = np.array([6, 7, 8, 9, 10])

results = arr + arr_1
multiplication = arr * arr_1
print("by the vectorization")
print(results)
print(multiplication)
