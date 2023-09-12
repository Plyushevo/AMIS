secret_number = 777


print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")


input_number = int(input('Enter a number here:'))

while input_number != secret_number:
    print("""

          HA-HA-HA
    YOU'VE STUCK IN MY LOOP
          
    """)
    input_number = int(input('Enter a number here:'))

print("""
      
"Well done, muggle! 
You are free now."

      """)