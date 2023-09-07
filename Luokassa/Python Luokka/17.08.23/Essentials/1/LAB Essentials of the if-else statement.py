income = float(input('Enter your income here:'))

if income > 85528:
  tax = round((14839.02 + (income - 85528) * 0.32), 1)
elif income > 0:
  tax = round((income * 0.18 - 556.02), 1)
# tax = round(x)
if tax < 0:
  tax = 0

print('your taxes are:', tax)