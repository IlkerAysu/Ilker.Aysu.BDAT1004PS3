#Step1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


#Step2-3
euro12 = pd.read_csv(r'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv') 
euro12.head()

df = pd.DataFrame(euro12)

#Step4
goals = euro12.set_index(['Goals'])
print(df['Goals'])

#Step5
prt = df['Team'].count()
print('Total participant is : ', prt)

#Step6
print("Total column number is : ", df.shape[1])

#Step7
discipline = df[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)

#Step8
yellow = discipline.sort_values(by='Yellow Cards', ascending=False)
print('YELLOW CARD SORT : ', yellow)

red =  discipline.sort_values(by='Red Cards', ascending=False)
print('Red CARD SORT : ', red)

#Step9
mean_yellow = discipline.groupby('Team').mean()
print(mean_yellow)

discipline1 = df[['Yellow Cards']]
mean_Avg = discipline1.mean()

print('Avg yellow cards:  ' , mean_Avg)

#Step10
offence = df[df['Goals'] > 6]
print(offence.head())

#Step11
print(df[df['Team'].str.startswith('G')])
#Step12
print(df.iloc[:, : 7])

#Step13
print(df.iloc[:, : -3])

#Step14
#??











