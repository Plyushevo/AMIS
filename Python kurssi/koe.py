def remainCalc(income, taxRate): #function that calculates remained money
  remain = income * (1 - taxRate / 100)
  return '{0:.2f}'.format(remain) # make 2 decimals digits

def taxCalc():
  while True:
    userInput = input("write your income in integer here: ") #user enter digits
    try: #handle value error
      userInput = int(userInput) # taxRate block
      if 0 <= userInput <= 5000:
        taxRate = 0
      elif 5000 < userInput <= 14000:
        taxRate = 15
      elif userInput > 14000:
        taxRate = 40
      else:
        print("Error negative income! Pls write a number over 0")
        continue
      print("Your income is", userInput, "your taxRate is", taxRate, "remained money after taxation:", remainCalc(userInput, taxRate) )#results
      break 
    except ValueError:
      print("Value error enter an integer number")

taxCalc()