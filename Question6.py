#Step1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt


#Step2-3

md = pd.read_csv(r'us-marriages-divorces-1867-2014.csv') 
md.head()

df = pd.DataFrame(md)

fig, ax = plt.subplots()

fig, ax1 = plt.subplots()
ax1.plot(df['Year'], df['Marriages'], 'o-g')
ax1.set_xlabel("Year")
ax1.set_ylabel("Marriages")
ax1.set_title("Marriage vs Divorce U.S. between 1867 and 2014")

# create ax2 with shared x-axis
ax2 = ax1.twinx()
# plot revenue on ax2
ax2.plot(df['Year'], df['Divorces'], '*-b')
ax2.set_ylabel("Divorces [$M]")

fig.legend(['Marriages', 'Divorces'], loc='upper left')
plt.show()
