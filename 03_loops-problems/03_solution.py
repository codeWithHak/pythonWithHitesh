# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = 3
for n in range(1,11):
    if n == 5:
        continue
    print(f"{number} x {n} = {number * n}")