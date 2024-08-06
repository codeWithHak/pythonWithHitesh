# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

user_age = input("What's your age: ")
day = input("What's the day: ")
int_user_age = int(user_age)

if int_user_age >= 18 and day == "wednesday":
        ticket_price = 10
        print(f"User Age: {int_user_age} Ticker Price: ${ticket_price}, Day: {day}")

elif int_user_age >= 18 and day != "wednesday":
        ticket_price = 12
        print(f"Ticket Price: ${ticket_price}, Day: {day}")

elif int_user_age <18:
    if day == "Wednesday" or "wednesday":
        ticket_price = 6
    else:
        ticket_price = 8
    print(f"Ticket Price: ${ticket_price}, Day: {day}")
    