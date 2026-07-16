# Airttificial Intelligence--->
# basic def - it is a fiel of cs that focus on creating machines that an think, learn and make decisions like humans

# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)

# 0-d arrays
# 1-d arrays

# import numpy as np
# arr = np.array(2)
# print(arr) #this is 0 dimentional array

# ar = np.array([1,2,3,4,5,6])
# print(ar) # this is 1 dimentional array

# ar2 = np.array([[1,2],[3,4],[5,6]])
# print(ar2) # this is the 2 dimentional array

# # 3d array - multiple of 2d arrays
# arr3 = np.array([
#     [1,2,3],
#     [3,2,1],
#     [
#         [1,2,3],
#         [2,3,4]
#     ]
# ])

# ndim ---> find the dimentions of array
# print(arr3.ndim)

# arr = np.array([1,2,3,4], ndim=5) #creates the 5-d array

# ARRAY INDEXING--->
# arr = np.array([1,2,3,4,5])
# print(arr[0])

# ar2 = np.array([[1,2],[3,4],[5,6]])
# ar2[0,1] #acess second element from first row

# arr3 = np.array([
#     [1,2,3],
#     [3,2,1],
#     [
#         [1,2,3],
#         [2,3,4]
#     ]
# ])
# arr[0,1,1]

# 3d = np.array([[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4]])
# 3d[1,1,2]

# slicing---->
# arr[1:2]
# arr2[0,1:2]
# arr3[1,1,0:4]

# dtype--->
# a = np.array([1,2,3,4,5])
# print(a.dtype) # shows array data type

# a = np.array([1,2,3,4,5], dtype="s") #thats creates only string data type array

# pip install pandas
# dataframes is a 2d structure, rows and columns

# import pandas as pd

# df = pd.dataFrame([1,2,3], columns=["numbers"])
# print(df)

# type()
# head()
# tail()
# print(df.shape)
# print(df.columns)
# rename()