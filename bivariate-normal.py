import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import statistics
import math
from mpl_toolkits.mplot3d import Axes3D

#read data
df = pd.read_excel(r"filepath") #file path of the excel data

#set axes values (x=column1, y=column2)
x_values = df['column1']
y_values = df['column2']
z_values = []
plot_points = []
z_score = []

#calculate correlation, std dev, mean for column1, column2
x_mean = statistics.mean(x_values)
y_mean = statistics.mean(y_values)
corr = df[['column1', 'column2']].corr()
corr = abs(corr['column1'].iloc[1])
x_dev = statistics.stdev(x_values)
y_dev = statistics.stdev(y_values)
print (x_dev, y_dev, x_mean, y_mean, corr)
x_var = (x_dev)**2
y_var = (y_dev)**2

#calculate z score for each x-y pair
for i in range(len(x_values)):
    x_calc = ((x_values[i]-x_mean)**2)/x_var
    y_calc = ((y_values[i]-y_mean)**2)/y_var
    combine_calc = (2*corr*(x_values[i]-x_mean)*(y_values[i]-y_mean))/(x_dev*y_dev)
    z = x_calc+y_calc-combine_calc
    z_score.append(z)

#calculate probability density
const=1/(2*math.pi*x_dev*y_dev*np.sqrt(1-corr**2))
for i in range(len(z_score)):
    exp=-z_score[i]/(2*(1-corr**2))
    z_values.append(const*math.exp(exp))

#create list of tuples to plot points
for i in range(len(x_values)):
    plot_points.append((x_values[i], y_values[i], z_values[i]))

fill_y=np.arange(min(df['Absolute Humidity (g/m³)']), max(df['Absolute Humidity (g/m³)']), 0.1)
fill_y=fill_y.astype(float)
for m in range(len(y_values)):
    for n in range(len(fill_y)):
        if y_values[m]==fill_y[n]:
            np.delete(fill_y, fill_y[n])
fill_y=fill_y.tolist()
print(fill_y)
        
fill_x=x_values.drop_duplicates(keep='first')

for i in range(len(x_values)):
    for j in range(len(fill_y)):
        plot_points.append((x_values[i], fill_y[j], 0))

for i in range(len(y_values)):
    for j in range(len(fill_x)):
        plot_points.append((fill_x.iloc[j], y_values[i] , 0))

#create graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x=[val[0] for val in plot_points]
y=[val[1] for val in plot_points]
z=[val[2] for val in plot_points]

ax.set_xlabel('column_1')
ax.set_ylabel('column_2')
ax.set_zlabel("Probability density")
ax.set_title("Bivariate normal distribution")

ax.plot_trisurf(x, y, z, cmap='viridis')
        
plt.show()
