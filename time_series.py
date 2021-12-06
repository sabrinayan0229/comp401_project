import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse
import matplotlib.dates as mdates

#read the file 
parser = argparse.ArgumentParser()
parser.add_argument('input', action='store', help='input file name')
args = parser.parse_args()
data = pd.read_csv(args.input, usecols=[0, 4],names =["Time", "Angle"])

data['Time'] = data['Time'].apply(lambda x: x/10)

print(data)
# data['Time'] = mdates.DateFormatter('%S')
# Make a data frame
time= data["Time"]
angle = data["Angle"]


plt.title('Time Series Graph ')
plt.xlabel('Time')
plt.ylabel('Angle')
'''
plt.ylim(-200,180)
plt.xlim(0,80)
'''
plt.plot_date(time,angle, linestyle='solid')
plt.tight_layout()
plt.show()

