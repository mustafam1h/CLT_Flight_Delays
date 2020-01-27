import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests
import matplotlib as mpl
import matplotlib.pyplot as plt





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
plt.show()