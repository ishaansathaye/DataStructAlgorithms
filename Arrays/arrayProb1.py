monthlyExpense = [['January', 'February', 'March', 'April', 'May'], [2200, 2350, 2600, 2130, 2190]]

# 1. In Feb, how many dollars you spent extra compare to January?

print()
print("$"+ str(monthlyExpense[1][1] - monthlyExpense[1][0]))
print()

# 2. Find out your total expense in first quarter (first three months) of the year.

total = 0
for i in range(0, 3):
    total = total +monthlyExpense[1][i]
print("Total: $"+str(total))
print()

# 3. Find out if you spent exactly 2000 dollars in any month

validMonths = []
for k in range(0, 5):
    if monthlyExpense[1][k] == 2000:
        validMonths.append(monthlyExpense[0][k])
if len(validMonths) != 0:
    for month in validMonths:
        print(month, "had exactly $2000!")
else:
    print("No month found with exactly $2000!")
print()

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

months = monthlyExpense[0]
months.append("June")
expenses = monthlyExpense[1]
expenses.append(1980)
print(monthlyExpense)
print()

# 5. You returned an item that you bought in a month of April and 
# got a refund of 200$. Make a correction to your monthly expense list based on this

monthlyExpense[1][3] = monthlyExpense[1][3] - 200
print(monthlyExpense)
print()