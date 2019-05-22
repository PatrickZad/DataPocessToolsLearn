import pandas as pd
import numpy as np
'''
Series
'''
series0=pd.Series([4,7,2,8,3,5,6,0],index=['a','f','g','h','r','t','q','o'])
#dict-like
print(series0['f'])
print(series0.keys())
print(series0.items())
#numpy array-like
print(series0['a':'r'])#explicit index is both sides closed,this op selects series['r] also
print(series0[0:5])
print(series0[(series0>3) & (series0<7)])
print(series0[['a','r']])
#indexer
print(series0.loc['a':'r'])#using explicit index,both sides closed also
print(series0.iloc[:3])#using implicit index
print(series0.ix[:5])#a mixed indexer , for series object it works like built-in list []
'''
DataFrame
'''
df0=pd.DataFrame(np.random.random((2,6)),index=['a','b'],columns=['q','w','e','r','t','y'])
print(df0)
#dict-like
print(df0['q'])#select a column
#2d-array-like
print(df0.values)
print(df0.T)
print(df0.values[0])#select a row
#indexer
print(df0.loc['a','q':'r'])#2d select
print(df0.iloc[:,:3])
print(df0.ix[0,'q':'t'])#mix indexer
print(df0.loc[df0.w>0.1,'w':'y'])#conditional select
#other 2d-array-like selection, select rows
print(df0['a':'b'])
print(df0[:])
print(df0[df0.w>0.1])