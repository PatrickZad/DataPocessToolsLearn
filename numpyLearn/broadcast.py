import numpy as np
'''
广播适用于不同型的数组（包括标量数字）运算，
运算的规则是补型至同型（低维向高维补，宽型和窄型同时补到同型，
并不在内存中真实做补型）
'''
'''
rule1:如果两数组维度数不同，那么低维度数组的形状将在最左边补1
rule2:如果两数组的形状在某一维度上不匹配，则形状将沿维度为1的维度扩展至匹配另一个数组
rule3:如果两数组形状在任何维度上都不匹配且没有数值为1的维度则引发异常
'''
array0=np.ones((2,6))
print(array0)
array1=np.ones(6)
print(array1)
#维度数不同，在array0最左补1，成为np.ones(1,6),维度数差的更多时继续补;
#(2,6)与(1,6)还有维度不匹配，沿1扩展成(2,6)则匹配
print(array0+array1)
array0=np.arange(3).reshape((3,1))
print(array0)
array1=np.arange(3)#按照rule1先补成(1,3),按照rule2再补成(3,3)
print(array1)
print(array1*array0)#array0按照rule2补成(3,3)


