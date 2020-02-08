#importing libraries
import statistics
import matplotlib.pyplot as plt
import pandas as pd
from random import sample

#extracting column of data
population=pd.read_excel(filename)
population=population["column_name"]

#initialise lists for data and means
column_name=[]
sample_means=[]

#set sampling parameters
number_of_samples=int(input("Enter number of samples: "))
sample_size=int(input("Enter sample size: "))

#converting the population into list form
for i in range(len(population)):
    column_name.append(population[i])
    
#sampling
for i in range(number_of_samples):
    x=statistics.mean(sample(column_name, sample_size))
    sample_means.append(x)

#calculating population and sample descriptives
print(statistics.mean(period))
print(statistics.variance(period))
print(statistics.mean(sample_means))
print(statistics.variance(sample_means))

#visualising the data
plt.hist(sample_means, bins=sqrt(sample_size))
plt.xlabel("Sample means")
plt.ylabel("Frequency")
plt.show()
