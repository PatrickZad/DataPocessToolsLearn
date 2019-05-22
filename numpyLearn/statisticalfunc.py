import numpy as np
data=np.random.random(10)
# sum,min,max,et al
# faster than built-in
# also can be called by '' arrayobject.max() ''
print(data)
print(np.sum(data))
print(data.max())
print(data.min())
#set axis,axis由小到大对应从外到内，
'''
作用是折叠某个维度
'''
data=np.random.random((4,5,6))
print(data)
print(data.max(axis=0))#data的最外层维度有四个，max从这四个中挑选最大值填到内层维度数组中，故结果是5*6的数组
print(data.min(axis=1))#4*6
print(data.sum(axis=2))#4*5
'''
there are also np.prod(product),np.mean,np.std(standared deviation),np.var(variance),et al.
'''
