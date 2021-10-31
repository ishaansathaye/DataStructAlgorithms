
#2. nyc_weather.csv contains new york city weather for first few days in the month of January. 
# Write a program that can answer following:
#a. What was the temperature on Jan 9?
#b. What was the temperature on Jan 4?
# Figure out data structure that is best for this problem

'''Read csv file'''
dictTempertures = {}
file = open("HashTable/HashTableProblems/nyc_weather.csv", "r")
next(file)
for line in file:
    elements = line.split(",")
    date = elements[0]
    temperature = int(elements[1])
    dictTempertures[date] = temperature

#a
print()
print("Temperature on Jan 9: " + str(dictTempertures["Jan 9"]))
print()

#b.
print("Temperature on Jan 4: " + str(dictTempertures["Jan 4"]))
print()

#Best data structure is a dictionary