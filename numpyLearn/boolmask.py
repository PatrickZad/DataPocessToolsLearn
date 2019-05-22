import numpy as np
'''
element-wise compare operators:==,!=,>,>=,<,<=
broadcast also supported
'''
array0=np.arange(6).reshape((6,1))
print(array0<=np.array(range(6)))
'''
useful functions,for a bool array,False equals 0 while True equals 1
'''
print(np.count_nonzero(array0<=np.array(range(6))))
print((array0<=np.array(range(6))).sum())#axis parameter also works
array0=np.random.random((2,6))
#all and any func
print(np.all(array0<0.5,axis=0))#关于axis参数，理解为折叠指定的维度，根据剩余的维度可以知道结果的形状，根据结果的形状可以知道比较的区域
print(np.any(array0<0.5,axis=1))
'''
bool operator:and,or,not;bit operators:&,|,~,^
'''
print((array0<0.2) ^ (array0>0.6))
print(((array0<0.2) ^ (array0>0.6)).sum())
'''
bool select
'''
print(array0[array0<0.5])
