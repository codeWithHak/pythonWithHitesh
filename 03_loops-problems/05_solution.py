# Problem: Given a string, find the first non-repeated character.

str = "aikthateeteraikbater"

for char in str:
    if str.count(char) == 1:
        print(char)
        break