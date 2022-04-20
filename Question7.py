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

df.plot(x="Year", y=["Marriages_per_1000","Divorces_per_1000"], kind="bar")


#