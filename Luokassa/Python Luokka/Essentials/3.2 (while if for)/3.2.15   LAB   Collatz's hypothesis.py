c0 = int(input('Enter any non-negative and non-zero integer number:'))

step_count = 0
intermediate_value = 0
while intermediate_value != 1:
  if c0 % 2 == 0:
    c0 /= 2
  else:
    c0 = 3 * c0 +1
  step_count += 1
  intermediate_value = int(c0)
  print(intermediate_value)
print('steps = ', step_count)




