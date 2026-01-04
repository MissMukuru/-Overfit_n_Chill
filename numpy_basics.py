import numpy as np
a = np.array([2,3,4])

print(a.dtype)

b = np.array([(1.3,2,3),(4,5,6)], dtype = complex)
print(b.dtype)

#to get the dimensions
print(a.ndim, a.shape, b.ndim, b.shape)

print(a.size)
#to now how much memory our arrays take up
print(a.itemsize * a.size) #this is how we get the total size of the array (a)

z = np.array([(1,2,3,4,5,6,7,8),(9,10,11,12,13,14,15,16)])
print(z.shape)
print(z[1,2])
print(z[0,-3])

#how to get a specific column
print(z[0: ,2]) #when inverted to print(z[0, :2]) it gives the first two elements to the first ist in the array

#we can access the elements inside the array using a step function
print(z[0, 1:6:2])
print(z[0, 1:-1:4])

print(z[0,2] == 20) #this returns a boolean value
z[0,2] = 20
print(z)

#Initialising all types of ARRAYS
p = np.zeros((2,3,3)) #this is a 3D array with the depth of 2, 3 rows and 3 columns
print(p)

o = np.ones((2,  5, 1), dtype= complex) #this is a 3D array with a block depth  of 2 and one column per row with 5 rows per block
print(o)

n = np.full((2,3) ,99) #this is 2 rows with 3 columns
print(n)

#the full_like element allows you to create another array that looks like a previously used array.
f = np.full_like(z, 4)
print(f)

#adding random interger values
p = np.random.rand(4,2) #this basically means that we create an array with 4 rows and 2 columns with random float points
print(p)

n  = np.random.randint(7, size = (3,3)) #take note of the syntax
print(n)

arr = np.array([[1,2,3,4], [2,4,5,6]])
rpt = np.repeat(arr, 2, axis = 0) #her we wor verticaly
print(rpt)

'''BASIC MATHEMATCAL COMPUTATIONS IN NUMPY'''



'''LINEAR ALGGEBRA 
IN 
NUMPY'''

