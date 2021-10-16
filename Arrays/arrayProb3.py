print()
oddList = []
maxNum = input("Enter the max number: ")
for i in range(0, int(maxNum)+1):
    if (i%2) != 0:
        oddList.append(i)
print(oddList)
print