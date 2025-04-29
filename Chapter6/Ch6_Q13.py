word1 = input("Enter the first string: ")
word2 = input("Enter another string with the same length: ")
newWord = ""
if (len(word1) == len(word2)):
    for i in range(len(word1)):
        newWord += word2[i]
        newWord += word1[i]
print(newWord)