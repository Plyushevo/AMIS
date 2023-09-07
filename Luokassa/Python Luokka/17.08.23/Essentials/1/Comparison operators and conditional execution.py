flower = input()

if flower == 'Spathiphyllum':
  print('Yes - Spathiphyllum is the best plant ever!')
  exit()
if flower == 'spathiphyllum':
  print('No, I want a big Spathiphyllum!')
  flower = input()
else:
  print('Spathiphyllum! Not', flower)
  flower = input()