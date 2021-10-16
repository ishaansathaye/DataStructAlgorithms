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

for k in range(0, 5):
    findAmount = monthlyExpense[1][k]
    if findAmount == 2000:
        exactMonth = monthlyExpense[0][i]
        found = True
        break
    else:
        found = False
if found == True:
    print(exactMonth, "had exactly $2000!")
else:
    print("No month found with exactly $2000!")
print()

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this