myWord = input("Type in a word: ")
myWordReverse = myWord[::-1]
if myWord == myWordReverse:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")