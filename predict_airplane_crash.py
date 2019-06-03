import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime
data = pd.read_csv('../socialite/airplane-crashes-since-1908/Airplane_Crashes_and_Fatalities_Since_1908.csv')
print(data.keys())
np.random.seed(50)
obs, feat = data.shape
print(obs)
print(feat)
print(data.sample(5))
result = data.isnull().sum()
print(result)
data['Time'] = data['Time'].replace(np.nan, '00:00')
data['Time'] = data['Time'].str.replace('c: ', '')
data['Time'] = data['Time'].str.replace('c:', '')
data['Time'] = data['Time'].str.replace('c', '')
data['Time'] = data['Time'].str.replace('12\'20', '12:20')
data['Time'] = data['Time'].str.replace('18.40','18:40')
data['Time'] = data['Time'].str.replace('0943','09:43')
data['Time'] = data['Time'].str.replace('22\'08', '22:08')
data['Time'] = data['Time'].str.replace('114.20', '00:00')
data['Time'] = data['Date'] + ' ' + data['Time']
def todate(x):
    return datetime.strptime(x, '%m/%d/%Y %H:%M') #format in particular manner
print(todate)
data['Time'] = data['Time'].apply(todate)
print('Date' + str(data.Time.min()) + str(data.Time.max()))
data.Operator = data.Operator.str.upper() # convert operator field in to capital
print(data.Operator)
print(data.Time.dt.year)
Temp = data.groupby(data.Time.dt.year)['Date'].count() #calculate which yar came how many times
Temp = Temp.rename(columns = {"Date":"Count"})
print(Temp.index)
plt.figure(figsize=(12,6))
plt.style.use('bmh')
plt.plot(Temp.index,Temp, color = 'blue', marker = '+', linewidth = 1) #as x year and as y counter here we did some change
plt.xlabel('year', fontsize = 10)
plt.ylabel('Count', fontsize = 10)
plt.title('accident count year', loc='Center', fontsize = 14)
plt.show()
import matplotlib.pylab as pl
import matplotlib.gridspec as gridspec
gs = gridspec.GridSpec(2, 2)
pl.figure(figsize=(15,10))
plt.style.use('seaborn-muted')
ax = pl.subplot(gs[0, :])
print(ax)
temp_month = data.groupby(data.Time.dt.month)['Date'].count()
sns.barplot(temp_month.index, temp_month , color = 'lightskyblue', linewidth=2)
plt.xticks(temp_month.index, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.xlabel('Month', fontsize = 10)
plt.ylabel('Count', fontsize = 10)
plt.title('accident count month', loc='Center', fontsize = 14)
plt.show()
