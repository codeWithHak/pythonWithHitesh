# Problem: Calculate the sum of even numbers up to a given number n.

n = 20
sum_of_even_num = 0

for i in range(1,20+1):
    if i%2 == 0:
        sum_of_even_num += 1
print(f"Sum of even number: {sum_of_even_num}")