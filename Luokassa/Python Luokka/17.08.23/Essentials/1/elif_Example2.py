# how to identify the larger of two numbers:

n1 = int(input('Enter the first integer number:'))
n2 = int(input('Enter the second integer number:'))
n3 = int(input('Enter the third integer number:'))

largerNumber = n1

if n2 > largerNumber:
  largerNumber = n2

if n3 > largerNumber:
  largerNumber = n3

print('Larger number is:', largerNumber)