from math import *
num = eval(input('Enter a number: '))
factorial = 1
for i in range (2,num+1):
    factorial *= i
print('The factorial of',num,'is',factorial)