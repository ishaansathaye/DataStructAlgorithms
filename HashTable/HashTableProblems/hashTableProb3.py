#3. poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
# You have to read this file in python and print every word and its count as show below. 
# Think about the best data structure that you can use to solve this problem. 
# Figure out why you selected that specific data structure.

wordDict = {}
file = open("HashTable/HashTableProblems/poem.txt", "r")
removeChar = ['-', ';', '.', ',', '!', ':']
for line in file:
    words = line.split(" ")
    for word in words:
        if word == '\n':
            words.remove(word)
        word = word.replace('\n', '')
        for char in removeChar:
            if char in word:
                word = word.strip(char)
        word = word.lower()
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

print(wordDict)
    