
name = input("Enter student name: ")

maths = float(input("Enter Maths marks out of 100: "))
computer = float(input("Enter Computer marks out of 100: "))
english = float(input("Enter English marks out of 100: "))

total = maths + computer + english
percentage = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total, "/ 300")
print("Percentage:", round(percentage, 2), "%")

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: F")
