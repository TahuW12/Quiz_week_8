import matplotlib.pyplot as plt
import pandas as pd

years = []
co2 = []
temp = []

# use pandas to open csv and read information

dataframe = pd.read_csv("climate.csv")

# use iteration to add all data to pre made arrays (years, co2, temp)

for data in dataframe["CO2"]:
    co2.append(data)
for data in dataframe["Year"]:
    years.append(data)
for data in dataframe["Temperature"]:
    temp.append(data)


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

