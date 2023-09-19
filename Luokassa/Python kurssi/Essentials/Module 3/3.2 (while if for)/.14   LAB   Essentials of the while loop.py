blocks = int(input('Enter a number of blocks in the pyramid:'))
height = 0
block_used = 0
step = 1

while block_used < blocks:
  block_used += step
  if block_used > blocks:
    break
  else:
    height += 1
    step += 1
      
  
  
print("The height of the pyramid:", height)


