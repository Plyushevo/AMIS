my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_new_list = []

for num in my_list:
  if num not in my_new_list:
    my_new_list.append(num)

my_list = my_new_list

print("The list with unique elements only:")
print(my_list)