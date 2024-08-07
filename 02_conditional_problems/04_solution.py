# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Apple"
fruit_color = "red"

if fruit_color == "Green" or fruit_color == "green":
    print(f"Fruit:{fruit}, Color:{fruit_color}, Condition:Unripe")

elif fruit_color == "Yellow" or fruit_color == "yellow":
    print(f"Fruit:{fruit}, Color:{fruit_color}, Condition:Ripe")

elif fruit_color == "Red" or fruit_color == "red":
    print(f"Fruit:{fruit}, Color:{fruit_color}, Condition:Overripe")