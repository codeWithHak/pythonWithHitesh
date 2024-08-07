# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

# my solution 18 lines of code

"""user_age = input("What's your age: ")
day = input("What's the day: ")
int_user_age = int(user_age)

if int_user_age >= 18 and day == "Wednesday" or "wednesday":
        ticket_price = 10
        print(f"User Age: {int_user_age} Ticker Price: ${ticket_price}, Day: {day}")

elif int_user_age >= 18 and day != "Wednesday" or "wednesday":
        ticket_price = 12
        print(f"Ticket Price: ${ticket_price}, Day: {day}")

elif int_user_age <18 and day == "Wednesday" or "wednesday":
        ticket_price = 6
        print(f"User Age: {int_user_age} Ticker Price: ${ticket_price}, Day: {day}")
elif int_user_age <18 and day != "Wednesday" or "wednesday":
        ticket_price = 8
        print(f"User Age: {int_user_age} Ticker Price: ${ticket_price}, Day: {day}")
"""    

# hitesh sir's solution

new_age = 19
new_price = 12 if new_age >= 18 else 8
new_day = "wednesday"
if new_day == "wednesday":
    new_price -= 2
    print(f"Your ticket price is: {new_price}")
else:
    print(f"Your ticket price is: {new_price}")