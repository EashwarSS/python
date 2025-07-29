import random

## We have random module in python, so we importing random module and using
## https://docs.python.org/3/library/random.html
## random_integer = random.randint(a, b)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
   print("Heads")
else:  
   print("Tails")