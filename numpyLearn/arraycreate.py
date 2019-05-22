'''
built-in array
'''
import array
numlist=list(range(10))
btarray=array.array('i',numlist)
'''
numpy array creation -> narray object
'''
import numpy as np
#from list
arrayfromlist=np.array([0.2,3,6,7])
arrayfloa=np.array([4,7,1,8,9],dtype='float32')
arraynd=np.array([range(i,i+6) for i in [2,6,8,9]])
#native creation
array0=np.zeros(10,dtype=int)
array1=np.ones((2,6),dtype=float)
array2=np.full((2,6),5.09)#fill in with given value
array3=np.arange(0,52,2)#start,end and step
array4=np.linspace(0,1,5)#evenly spaced
array5=np.random.random((6,6))#get random floats in interval [0.0,1.0) in given size
array6=np.random.normal(0,52,(6,6))#given interval and size,get random floats subject to normal distribution
array7=np.random.randint(0,52,(6,6))
array8=np.eye(6)
array9=np.empty(6)
