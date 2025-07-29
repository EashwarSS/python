import random

## We have random module in python, so we importing random module and using
## https://docs.python.org/3/library/random.html

friends = ["Anirudh", "Eashwar", "Shravika", "Mounika"]

# Option 1
print(random.choice(friends))

# Option 2
random_friend = random.randint(0, 3)
print(friends[random_friend])