"""
broadcasting -> its is the numpy way which is perform operation in the 
different different arrays size without using loops

needs -> mathematical problems which is need to solve in array's
which is different in size.
"""

# problem

prices = [100,200,300]
discount = 10 #10%
final_prices = []
for price in prices:
    final_price = price - (price * discount / 100)
    final_prices.append(final_price)
print(final_prices)
# this is the very slow thatwhy broadcast is introduce

import numpy as np

prices = np.array([100,200,300])
discounts = 10
final = prices - (prices * discount / 100)
print(final)

"""
how numpy handle array of different shapes
-> 
1. matching dimensions
2. expanding single elements
3. incompatible shapes -> error
"""
# example
arr  = np.array([100,200,300,400,500])
result = arr * 2
print("broadcasting single value")
print(result)

print("\n")

matrix = np.array([[1,2,3],[4,5,6]])     #2X3 matrix
vector = np.array([10,20,30])
result = matrix + vector
print("matching dimension")
print(result)

#error incompatible shapes

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([1,2])
print("error -> incompatible shapes")
result1 = arr1 + arr2
print("error -> incompatible shapes")
print(result1)
