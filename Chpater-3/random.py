# we will see how we can chosse random number
import random
from random import choice

letters = "abcdefghijklmnopqrstuvwxyz1234567890"

# Pythonic version
item = random.choice(letters)
print("This is random letter ", item)
