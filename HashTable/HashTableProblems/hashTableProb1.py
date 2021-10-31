# 1. nyc_weather.csv contains new york city weather for first few days in the month of January. 
# Write a program that can answer following:
# a. What was the average temperature in first week of Jan
# b. What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

#a
'''Read csv file'''
listTemperatures = []
file = open("HashTable/HashTableProblems/nyc_weather.csv", "r")
next(file)
for line in file:
    elements = line.split(",")
    temperature = int(elements[1])
    listTemperatures.append(temperature)
sum = 0
for i in range(0,7):
    sum += listTemperatures[i]
print()
print("First Week Average: " + str(round(sum/7, 2)))
print()

#b.
print("Max Temperature 10 days: " + str(max(listTemperatures[0:10])))
print()

#Best data structure is a list