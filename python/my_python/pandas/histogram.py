import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({ 'length': [1.5, 0.5, 1.2, 0.9, 3, 4, 5],
                    'width': [0.7, 0.2, 0.15, 0.2, 1.1,2,3]
                  }, index= ['pig', 'rabbit','duck', 'chicken', 'horse','dog','cat'])

#print(df['width'])
#print(len(df['width']))
#print(max(df['width']))

#print(df['length'])

#hist = df.hist(bins=3)
df['length'].hist(bins=5)
''' If bins is an interger bins will be the range of value, each value in the range will be 1 bin.
If bins is an sequence [0, 10, 20, 30, 100] each group of value will be 1 bin. 0to10 is first bin, 10to20 will be second, last will be 30to100'''
#df['width'].hist(bins= max(df['width']) - min(df['width']),align='left') # x axis is value, y axis is the numbers of value
plt.show()
