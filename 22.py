web_stats={'Day':[1,2,3,4,5,6],
           'Visitors':[43,34,65,56,29,76],
           'Bounce Rate':[65,67,78,65,45,52]}

import pandas as pd

web_stats={'Day':[1,2,3,4,5,6],
           'Visitors':[43,34,65,56,29,76],
           'Bounce Rate':[65,67,78,65,45,52]}

df=pd.DataFrame(web_stats)

print(df.head())

print(df.tail())

print(df.tail(2))

df.set_index('Day', inplace=True)



# df=df.set_index('Day')

import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

print(df['Visitors'])

print(df.Visitors)

df['Visitors'].plot()
plt.show()




df.plot()
plt.show()

print(df[['Visitors', 'Bounce Rate']])

print()
print()












