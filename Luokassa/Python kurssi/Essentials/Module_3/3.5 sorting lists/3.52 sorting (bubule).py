my_list = []
swapped = True
num = int(input('How many numbers do you want to sort?:'))

for i in range(num):
  val = int(input('Enter a number:'))
  my_list.append(val)

while swapped:
  swapped = False
  for i in range(len(my_list)- 1):
    if my_list[i] > my_list[i + 1]:
      swapped = True
      my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print('Sorted: ', my_list)


my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)