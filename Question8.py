#Step1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt


#Step2-3

ak = pd.read_csv(r'actor_kill_counts.csv') 
ak.head()

ak_sorted = ak.sort_values('Count')

colours = ['#C4E57D','#2AC280','#FFAE39','#DC5B3B','#52E397','#C5CBA3','#9CD5F6','#6E50D9','#9A5E59','#9BC8F5']
ak_sorted['Count'].value_counts().sort_index().plot.barh(color=colours)




# df.plot(x="Year", y=["Marriages_per_1000","Divorces_per_1000"], kind="bar")
# df['Count'].value_counts().sort_index().plot.barh()
# ak.plot.barh(x=ak['Count'], y=ak['Actor'], title='Deadliest Actor', color='blue')


ax = ak_sorted.plot(x="Actor", y="Count", kind="barh")
# plotting age on the same axis
