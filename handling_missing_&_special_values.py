"""
why? -> with the work of real data its also deal with missing
and incorrect values example filling form.

3 function's
np.isnan() -> detect missing value's
np.nan_to_num() -> replace the value's
np.isinf() -> use to detect infinite value's

*imp
"""
import numpy as np

#np.isnan()
arr = np.array([1,2,np.nan,4,5,np.nan,7,8,9,10])
print("is nan")
print(np.isnan(arr))

# print(np.nan == np.nan) is not directly compare

#np.nan_to_num(array, nan=value) default - 0,   not process ML modules
print("replace")
clearned_arr = np.nan_to_num(arr,nan=100)
print(clearned_arr)


#np.isinf()
print("np.isinf()")
arr_1 = np.array([1,2,np.inf,4-np.inf,6])
print(np.isinf(arr_1))

print("infinite replace")
clearned_arr_2 = np.nan_to_num(arr_1, posinf= 1000,neginf = -1000)
print(clearned_arr_2)