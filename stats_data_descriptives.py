import statistics
import matplotlib.pyplot as plt
import pandas as pd
from random import sample

population=pd.read_excel(r"C:\Users\vibha\Documents\PSC.xlsx")
population=population["Period (ms)"]
period=[]
sample_means=[]

for i in range(len(population)-1):
    period.append(population[i])
print(statistics.mean(period))
print(statistics.variance(period))

for i in range(2000):
    x=statistics.mean(sample(period, 30))
    sample_means.append(x)

print(statistics.mean(sample_means))
print(statistics.variance(sample_means))
plt.hist(sample_means, bins=80)
plt.show()

