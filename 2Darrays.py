import numpy as np3
#2D arrays

from_list = np3.array([[1,2,3],[4,5,6]], dtype=np3.int8)
array_2d = np3.array((np3.arange(0,8,2), np3.arange(1,8,2)))
#print(from_list)
array_2d = array_2d.reshape((4,2))


print(array_2d) #first array prints even digits and second array prints odd digits

print("2D shape:", array_2d.shape) #confirm it is a 2d array
