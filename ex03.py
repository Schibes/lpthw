# Practice some basic math in Python. Heading:
print("I will now count my chickens:")

# Hens will be 30 because division happens first
print("Hens", float(25 + 30 / 6))

# Roosters has some modulus math in there.
# Mod has same PEMDAS precedence as multiply/divide.
# 75 mod 4 = 3
print("Roosters", float(100 - 25 * 3 % 4))

# More blather
print("Now I will count the eggs:")

# This works out to 6.75 because 4 mod 2 = 0. 
print(float(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6))

# Just prints stuff
print("Is it true that 3 + 2 < 5 -7?")

# does the 3 + 2 and 5 - 7 parts then compares them
print(3 + 2 < 5 - 7)

# Uses commas to concatenate more stuff to print
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

# Yeah Zed
print("Oh, that's why it's False.")

# More Zed blather
print("How about some more.")

# More concatenation
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)