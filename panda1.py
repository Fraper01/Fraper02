import pandas as pd
import numpy as np

name_age = {'Name' : ['Ali', 'Bill', 'David', 'Hany', 'Ibtisam'],
'Age' : [32, 55, 20, 43, 30]}
data_frame = pd.DataFrame(name_age)
print (data_frame)
data_frame_2 = pd.DataFrame(name_age, columns = ['Age', 'Name'], index = ['a', 'b', 'c', 'd', 'e'])
print (data_frame_2)

series = pd.Series(['Ali', 'Bill', 'David', 'Hany', 'Ibtisam'],
index = [1, 2, 3, 4, 5])
print (series)

series = pd.Series(np.random.randn(20000))

print (series.head())
print (series.tail(20))

lista = ('Ali', 'Bill', 'David', 'Hany', 'Ibtisam','Francisco')
data_frame = pd.DataFrame(lista, index = ['a', 'b', 'c', 'd', 'e','f'])
print (data_frame)

data_frame.describe()
data_frame_2.describe()

name_age = {'Name' : ['Ali', 'Bill', 'David', 'Hany', 'Ibtisam','Francisco'],
'Age' : [32, 55, 20, 43, 30,62]}
data_frame3 = pd.DataFrame(name_age)
print (data_frame3)
print (data_frame3.describe())
data_frame3.info(show_counts=True, memory_usage=True, verbose=True)

print(data_frame3.shape) # Get the number of rows and columns
print(data_frame3.shape[0]) # Get the number of rows only
print(data_frame3.shape[1]) # Get the number of columns only

print (data_frame3.columns)

print (list(data_frame3.columns))



