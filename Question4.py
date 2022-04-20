#Step1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


#Step2-3
wind = pd.read_csv(r'wind.txt') 
wind.head()

df = pd.DataFrame(wind)


df.fillna('',inplace=True)
print(df.head())

df[['Yr', 'Mo', 'Dy', 'RPT', 'VAL', 'ROS', 'KIL', 'SHA', 'BIR', 'DUB', 'CLA', 'MUL', 'CLO', 'BEL', 'MAL']] = df['Yr Mo Dy   RPT   VAL   ROS   KIL   SHA   BIR   DUB   CLA   MUL   CLO   BEL   MAL'].str.split(' ', 14, expand=True)

deneme = df.describe()
print(deneme)

# print(users.head())

# df[['user_id', 'age', 'gender', 'occupation', 'zip_code']] = df['user_id|age|gender|occupation|zip_code'].str.split('|', 4, expand=True)
