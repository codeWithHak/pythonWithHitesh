# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

input = input("Tell me your marks: ")
result = int(input)

if result < 60:
    print("F")

elif result <70:
    print("D")

elif result < 80:
    print("C")

elif result < 90:
    print("B")

elif result < 100:
    print("A")