import numpy as np
array0=np.arange(6)
'''
list/array index
the selected array share its shape with index array
'''
indexlist=[0,3,5]
print(array0[indexlist])
indexarray=np.array([[0,2],[3,5]])
print(array0[indexarray])
'''
for high dementional array
'''
array0=np.random.random((6,6))
rowindex=np.array([1,2,6])
columnindex=np.array([0,3,5])
#actually select (1,0),(2,3),(6,5)
print(array0[rowindex,columnindex])#此处行索引向量和列索引向量是形状匹配的故可以直接select
'''
行索引和列索引形状不匹配时会引发broadcast机制来匹配
'''
columnindex=np.array([0,3,5]).reshape((3,1))
print(array0[rowindex,columnindex])
'''
同理索引可以用标量和array索引broadcast，
'''
'''
索引同样适合修改数组元素，注意重复的索引会使先赋的值被覆盖，对应可以理解索引的结果并不是原array的副本，而是一个部分视图
'''
