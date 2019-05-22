import numpy as np
array0=np.array([2,8,6,9,10])
'''
产生一个新的array作为排序结果，不改变原array，默认quick sort
'''
print(np.vstack([array0,np.sort(array0)]))
'''
直接对原array排序，默认quick sort
'''
array0.sort()
print(array0)
'''
返回按值排序的索引array
'''
array0=np.array([2,8,6,9,10])
indexsort=np.argsort(array0)
print(array0[indexsort])
'''
按维度排序，是对指定的axis维度内的元素为单位相互比较的排序
'''
array0=np.random.RandomState(42).randint(0,10,(4,5,6))
print(array0)
print(np.sort(array0,axis=0))
print(np.sort(array0,axis=1))
print(np.sort(array0,axis=2))
'''
寻找前k小的一组元素，同样支持指定axis,返回的是array,前k小元素为结果的前k个元素
'''
print(np.partition(array0,2,axis=0))
print(np.partition(array0,2,axis=2))
'''
同理有np.argpartition
'''