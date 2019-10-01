import pandas as pd 
import numpy as np

df = pd.DataFrame({
    'city': ['osaka', 'osaka', 'osaka', 'osaka', 'tokyo', 'tokyo', 'kyoto'],
    'food': ['apple', 'orange', 'banana', 'banana', 'apple', 'apple', 'banana'],
    'price': [100, 200, 250, 300, 150, 200, 400],
    'quantity': [1,2,3,4,5,6,7]})

print(df)
print('\nsum', df.sum())
print('\nget only 3 cols')
print(df.head(n=3))
print('\ndrop city col')
print(df.drop('city', axis = 1))
print('\nget only axis 0')
print(df.query('index == 0'))
print('\nuse query with condition')
print('city == "osaka" or city == "tokyo"')
print(df.query('city == "osaka" | city == "tokyo"'))
print('price== 200 and food == "banana"')
print(df.query('price == 250 & food == "banana"'))

#print(df.columns)
#print(df.index)

# show grouped data from data frame
#print(df.groupby('city'))
#print(df.groupby('city').mean())
#print(df.groupby(['city', 'food']).mean())
#print(df.groupby(['city', 'food'], as_index=False).mean())

# show label properties from data frame
#print(df.groupby('city').groups)
#print(df.groupby('city').get_group('osaka'))
#print(df.groupby('city').size())
#print(df.groupby('city').size()['osaka'])


########## Aggregation mean calculating values from each group and then make new group
#print(df.groupby('city').agg(np.mean)) # creating new group of mean value from old group
def my_mean(s):
    return np.mean(s)
#print (df.groupby('city').agg({'price': my_mean, 'quantity':np.sum})) # creating new group from old group using func
#print(df.groupby(['city', 'food'], as_index=False).apply(lambda d: (d.price * d.quantity).sum()))
#print(df.groupby(['city', 'food'], as_index=False).apply(lambda d: d.name))

def total_series(d):
    print('\ninisde_funct:')
    print(d)
    return d.price * d.quantity
#print(df.groupby(['city','food']).apply(total_series))

def total_keepindex(d):
    return pd.DataFrame({'total': (d.price * d.quantity).sum()}, index=['hi'])

print(df.groupby(['city', 'food']).apply(total_keepindex))

def transformation_sample(s):
    return (s/s.sum()*100).astype(str)+'%'
print(df.groupby(['city']).transform(transformation_sample))
