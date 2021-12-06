from datetime import timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

df=pd.read_csv('out.csv',usecols=[0, 4],names =["Time", "Angle"])
df = df.iloc[1: , :]
df= df.astype("float64")

#rename the first column and calculate the time 
df.rename( columns={'Unnamed: 0':'Time'}, inplace=True )
df['Time']= df['Time'].apply(lambda x: x/10)

# print(df)'''

plt.title("Time VS. Angle Autocorrelation Graph")
autocorrelation_plot(df).set_xlim([0, 50])
plt.show()




