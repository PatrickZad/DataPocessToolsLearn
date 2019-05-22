import pandas as pd
import numpy as np
'''
Series Object
'''
#creation
data0=pd.Series(range(8))#from list
print(data0)
data1=pd.Series(np.array(range(8)))#from numpy array
print(data1)
data2=pd.Series(6,index=['a','e','o'])#from scalar,auto-fill
print(data2)
datadict={'a':0,'b':1,'c':2,'f':3,'d':4,'e':5}
data=pd.Series(datadict)#from dict
print(data)
#important property
print(data.values)
print(data.index)
#index
print(data['a':'d'])
#index user-defined array
data=pd.Series(range(6),index=['a','b','c','d','e','f'])
print(data)
'''
DataFrame Object
'''
#creation
df=pd.DataFrame({'column0':data0,'column1':data1})#from Serise dict
print(df)
df1=pd.DataFrame(data0,columns=['column0'])#from one Series object
print(df1)
df2=pd.DataFrame([{'a':2,'b':6},{'b':2,'c':8}])#from a list of dict,missing data will be shown as NaN
print(df2)
df3=pd.DataFrame(np.random.random((2,6)),index=['a','b'])#from 2-dementional array,index and columns can be user defined while the default are ascending int numbers
print(df3)
#important property
print(df.index)
print(df.columns)
'''
Index Object
'''
#creation
indexobj=pd.Index([3,6,1,7,8,3])
print(indexobj)
#important properties
print(indexobj.size,indexobj.shape,indexobj.ndim,indexobj.dtype)#note that index is a column vector,so shape is (6,1)
'''
#index is constant
indexobj[2]=1
'''
#set operations
indexobj1=pd.Index([8,3,8,3,6,8,2,1,1])
print(indexobj & indexobj1)
'''
print(indexobj | indexobj1)#only valid with uniquely valued Index objects
'''
print(indexobj ^ indexobj1)