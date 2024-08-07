# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = "Dog"
pet_age = 3

if pet == "dog" and pet_age < 3:
    print("puppy food")

elif pet == "dog" or pet == "Dog" and pet_age > 2:
    print("senior dog food")

elif pet == "cat" and pet_age < 3:
    print("kitten food")

elif pet == "cat" and pet_age > 2:
    print("senior dog food")