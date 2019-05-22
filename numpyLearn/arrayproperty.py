import numpy as np
np.random.seed(1)
array0=np.random.randint(10,size=6)
array1=np.random.randint(10,size=(2,3))
array2=np.random.randint(10,size=(2,3,4))
#property
print(array2.ndim)#dimension
print(array2.shape)#length of dimensions,exernal to internal
print(array2.size)#total length
print(array2.dtype)#datatype of the numbers

#get
print(array0[-2])
print(array2[1,2,3])

#slice-----return refernce rather than a copy,carful to change
print(array0[::2])#step
print(array0[::-2])#step and reverse
print(array2[:,:2,1:3])#every dimension sliced,step and reverse are also supported

#row
print(array1[1])
print(array1[1,:])

#column
print(array1[:,1])

#create copy
copy1=array1[1,:].copy()

#reshape
print(np.arange(1,10).reshape((3,3)))
array0=array0.reshape((6,1))
array0=array0[np.newaxis,:]#to row vector,can add axis
array0=array0[:,np.newaxis]#to column vector,can add axis
array0=array0.reshape((1,6))#can change axis

#split
x0,x1,x2=np.split(array0,(2,5))
upper,lower=np.vsplit(array1,(2,))
lefty,right=np.hsplit(array1,(2,))

#connect
array3=array0.copy()
array3=np.concatenate([array0,array3])
array3=array1.copy()
array3=np.concatenate([array1,array3],axis=1)#axis can be changed,numpy has specification for axis concept
array3=np.hstack([array1,array3])
array3=array1.copy()
array3=np.vstack([array1,array3])
array3=array2.copy()
array3=np.dstack([array2,array3])
