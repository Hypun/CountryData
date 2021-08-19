import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
class Stats:
    countries: object = pd.read_excel(r"D:\Project_File.xlsx")
#122-241
Stats()
Cunt_List=[13, 14, 15, 16, 17, 18, 30, 31, 32, 33, 34]
print(Stats.countries)
df = Stats.countries
df = df.iloc[:,lambda df:[0,13, 14, 15, 16, 17, 18, 30, 31, 32, 33, 34]]
df2 = df.set_index('Unnamed: 0')
df2 = df2.loc['1988 Jan':'1997 Dec']
print (df2)
Sums = df2.sum(axis=0)
Sums = Sums.sort_values(ascending=True)
print (Sums)
mos1 = Sums.index[0]
mos2 = Sums.index[1]
mos3 = Sums.index[2]
print("The top 3 countries with the least visitors are", mos1 , mos2 , mos3)


vis1 = Sums[mos1]
vis2 = Sums[mos2]
vis3 = Sums[mos3]
print("The Amount of visitors from the Lowest 3 countries are", vis1 , vis2 , vis3, "respectively")


means = df2.mean(axis=0)
means = means.sort_values(ascending=True)
print (means)
mean1 = round(means[0],2)
mean2 = round(means[1],2)
mean3 = round(means[2],2)
print("The Average visitors from the Lowest 3 countries are", mean1 , mean2 , mean3, "respectively")


medians = df2.median(axis=0)
medians = medians.sort_values(ascending=True)
print (medians)
med1 = medians[0]
med2 = medians[1]
med3 = medians[2]
print("The Median visitors from the Lowest 3 countries are", med1 , med2 , med3, "respectively")




date_sum = df2.sum(axis=1)
months = np.zeros((12,), dtype=int).tolist()
month_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for j in range(0,12):
    for i in np.arange(j,120,12):
        months[j] += date_sum.iat[i]
print (months)
plt.plot(month_names,months)

date_sum = df2.median(axis=1)
months = np.zeros((12,), dtype=int).tolist()
month_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for j in range(0,12):
    for i in np.arange(j,120,12):
        months[j] += date_sum.iat[i]
print (months)
plt.bar(month_names,months)





