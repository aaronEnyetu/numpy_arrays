#Reshaping array: We can use reshape method to reshape an array. Consider an array with shape (a1, a2, a3, …, aN). 
#We can reshape and convert it into another array with shape (b1, b2, b3, …, bM).
# The only required condition is: a1 x a2 x a3 … x aN = b1 x b2 x b3 … x bM . 
#(i.e original size of array remains unchanged.) numpy.reshape(array, shape, order = ‘C’) :
# Shapes an array without changing data of array.

import numpy as resh

array = resh.arange(8)
print("Original array: \n", array)


#shape array with 2 rows and 4 columns
array = resh.arange(8).reshape(2,4)
print("\narray reshaped with 2 rows and 4 columns: \n", array)

#shape array with 4 rows and 2 columns
array = resh.arange(8).reshape(4,2)
print("\narray reshaped with 4 rows and 2 columns: \n", array)


#COnstruct 3D array
array = resh.arange(8).reshape(2,2,2)
print("\nOriginal array reshaped to 3D: \n", array)