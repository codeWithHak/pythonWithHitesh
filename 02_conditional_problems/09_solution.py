# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

input = input("What year is it: ")
year = int(input)

if year % 4 == 0 and year % 100 != 0 or year % 100 == 0:
    print("it is a leap year")

else:
    print("not a leap year")