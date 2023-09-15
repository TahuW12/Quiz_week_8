import matplotlib.pyplot as plt

#use sqlite3 library to connect to database
import sqlite3



years = []
co2 = []
temp = []

#write some code in climate_q1.py to connect to database,
#fetch the values, and populate python lists wiht corresponding values.

# connect to db
con = sqlite3.connect('climate.db')

#make a cursor for executing sql 

cursor = con.cursor()

# Fetch data from the database

cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData ORDER BY Year")


#create tables array containing all data in climate.db
tables = cursor.fetchall()

#check content of tables

#print(tables)

# iterate through tables, filling the years, co2, and temp arrays

for table in tables:
    years.append(table[0])
    co2.append(table[1])
    temp.append(table[2])

# Close connection to db
con.close()





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
plt.savefig("co2_temp_1.png") 
