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