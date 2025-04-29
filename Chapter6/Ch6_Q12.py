myWord = input("Enter a word: ")
myWordCaps = myWord.upper()
newWord = ""
for i in range(len(myWord)):
    if (i%2 == 0):
        newWord += myWord[i]
    else:
        newWord += myWordCaps[i]
print(newWord)