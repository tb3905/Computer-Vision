import numpy as np
#np.random.seed(int) use to not change value after every run 
np.random.seed(55)
ar=np.random.randint(0,1000,50)
print(ar)
#.reshape use for reshape the matrix 
a1=ar.reshape(5,10)

np.random.seed(5)
br=np.random.randint(0,200,25)
print(br)
np.random.seed(1)
cr=np.random.randint(1,256,64).reshape(8,8)
#give you the max value of matrix
print(cr.max())
#give you min value of matrix
print(cr.min())
#mean value of array or matrix
print(cr.mean())
#maximum value position
print(cr.argmax())
#minimum value position
print(cr.argmin())
#shape of array
print(cr.shape)
print(cr)
#value at given position
r=0
c=0
print(cr[r,c])
print(cr[:,c])
print(cr[r,:])
print(cr[0:2,1:4])

#coping arr in drr
dr=ar.copy()
print(dr)
