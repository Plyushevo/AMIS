secret_word = 'chupacabra'

while True:
  word = str(input('Enter the word here:'))
  if word == secret_word:
    print('"You\'ve successfully left the loop."')
    break
