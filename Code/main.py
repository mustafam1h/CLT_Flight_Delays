import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np





def load_csv_df():
  csv_df = pd.read_csv('../Data/Data.csv')
  csv_df = csv_df.drop(csv_df.columns[0], axis=1)
  return csv_df

data = load_csv_df()
print (data.head(10))

flight_name=list(data['name'].unique());
flight_name.sort()
#Get the flight name sored 


def plot(df,col,ax):
  mpl.style.use('default')
  ## Subset the data frame to the flight of concern 
  #data = flights[flights['name'] == 'Alaska Airlines Inc.'] as example for the first iteration
  data=df[df['name']==col]
  # Draw the density plot
  f = sns.distplot(data['arr_delay'], hist = False, kde = True,
                 kde_kws = {'linewidth': 3},
                 label = col)
  # Fix the plot dimensions to make the airlines easier comparable
  f.set(xlim=(-75, 125))
  f.set(ylim=(0, 0.0275))
  #Plot formatting
  ax.legend(prop={'size': 4}, title = '')
  
plt.figure(figsize=(10,120))
i=0
for flight in flight_name:
    ax = plt.subplot(len(flight_name),1 ,1+i)
    plot(data,flight,ax)
    i=i+1
	#plt.show() uncomment this line if you want to see each pdf alone 
plt.show()

plt.figure(figsize=(80, 10))
sns.boxplot(x='name',y='arr_delay',data=data)
plt.show()


#check flight with maximuim number of arriving before or before delay 
maxname = ''
max_num = 0
for name in flight_name:
  nums = data[data['name'] == name]['arr_delay']
  counts = nums.apply(lambda x:1 if x <= 0 else 0)
  count = counts.sum()
  if max_num < count / nums.count():
    max_num = count / nums.count()
    maxname = name
print(maxname)


mean_all = data['arr_delay'].mean()
std_all = data['arr_delay'].std()
print(mean_all,std_all)

def GaussianPlot(means,ax,sample):
  f=sns.distplot(means,kde=True,ax=ax,label='mean: '+ str(np.array(means).mean()) + ' std: '+str(np.array(means).std()))
  f.set(xlim=(-50, 50))
  ax.set_title('Histogram of mean with sample size = %d' % sample, size = 10)
  ax.set_xlabel('Delay (min)', size = 15)
  ax.set_ylabel('Flights', size= 15)
  ax.legend()
 

samples_size = [10,100,1000,10000]
i=0
fig,axes = plt.subplots(2,2,figsize=(30,10))
axes = axes.flatten()
for sample in samples_size:
  means = []
  for _ in range(100):
    idx = np.random.choice(data.count()[0],sample)
    nums = data.iloc[idx]['arr_delay']
    means.append(nums.mean())
  GaussianPlot(means,axes[i],sample)
  i=i+1
plt.show()
#print(data.count()[0])

