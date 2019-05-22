import numpy as np
'''
faster element-wise computation
'''
array=np.arange(6)
# basic operators
print(array)
print(array+5)
print(array*2)
print(-array)
print(array**3)
# abs,sin,cos,log,exp,et al
array=np.array([-1,2,-3,4,-5,6])
print(np.abs(array))#complex numbers are also supported
# special functions
from scipy import special
print(special.gamma(array))#Gamma function
print(special.erf(array))
'''
advanced:compute functions have more power
'''
# given output direction,
# compare to compute (temporarily store the result) 
# and set value,this can save one step
x=np.arange(6)
y=np.empty(6)
np.multiply(x,10,out=y)#use out parameter
print(y)
y=np.zeros(12)
np.power(2,x,out=y[::2])#more trick

#reduce,works for compute functions
x=np.arange(6)
print(np.add.reduce(x))
print(np.add.accumulate(x))#save the medium results and composes an array

#every pair compute
x=np.arange(6)
print(np.multipy.outer(x,x))
