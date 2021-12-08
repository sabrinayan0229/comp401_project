#Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

directory = '/Users/sebastian/Documents/Hendricks Lab/Python Analysis/'
df = pd.read_csv(directory + 'all_angles_-outliers.csv',index_col = 0)
df = df.iloc[1: , :]
df= df.astype("float64")

names = list(df.columns.values)
#print(names[0:5])
x = df[names[0]]
y1 = df[names[1]]
y2 = df[names[2]]
y3 = df[names[3]]
y4 = df[names[4]]
y5 = df[names[5]]

plt.style.use('seaborn-darkgrid')
# create a color palette
palette = plt.get_cmap('rainbow_r')
 
# multiple line plot
num=0
for column in df.drop('Time', axis=1):
    num+=1
 
    # Find the right spot on the plot
    plt.subplot(4,4, num)
 
    # plot every group, but discrete
    #plt.plot(df['Time'], df[column], marker='', color=palette(num*10), linewidth=1.9, alpha=0.9, label=column)
 
    # Plot the lineplot
    plt.plot(df['Time'], df[column], marker='', color=palette(num*15), linewidth=2.4, alpha=0.9, label=column)
 
    # Same limits for every chart
    plt.xlim(0,60)
    plt.ylim(-100,100)
 
    # Not ticks everywhere
    if num in range(7) :
        plt.tick_params(labelbottom='off')
    if num not in [1,4,7] :
        plt.tick_params(labelleft='off')
 
    # Add title
    plt.title(column, loc='left', fontsize=12, fontweight='bold', color=palette(num) )

# general title
plt.suptitle("Example Headswings in various Phenotypic Backgrounds", fontsize=13, fontweight=0, color='black', style='italic', y=1.02)
 
# Axis titles
#plt.text(0.5, 0.02, 'Time', ha='center', va='center')
#plt.text(0.06, 0.5, 'Head Angle (°)', ha='center', va='center', rotation='vertical')

# Show the graph
plt.show()
#plt.savefig(directory + 'autocorrelation.png')