list = [12, 11, 10, 9, 8, 7, 6, 5]
to_find = int(input('Enter a number to find:'))
found = False

for i in range(len(list)):
  found = to_find == list[i]
  if found:
   break

if found:
  print('Your number was found at index:', i)
else:
  print('Your number is absent in the list')
