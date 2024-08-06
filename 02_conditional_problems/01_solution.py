# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# my solution

"""
person_age = 13

if person_age < 13:
    print("Child")

if person_age >= 13 and person_age <=19:
    print("Teenager")

if person_age >= 20 and person_age <= 59:
    print("Adult")   


if person_age > 60:
    print("Senior")"""


# Sir Hitesh's BETTER solution

user_input = input("What's your age: ")
int_user_input = int(user_input)

if int_user_input < 13:
    print("Child")

elif int_user_input < 20:
    print("Teenager")

elif int_user_input < 60:
    print("Adult")

else:
    print("Senior")