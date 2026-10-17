
print("=" * 40)
print("      STUDENT RESULT SYSTEM")
print("=" * 40)

name = input("Enter student name: ").strip()
roll_no = input("Enter roll number: ").strip()

while not name:
    print("Name cannot be empty.")
    name = input("Enter student name: ").strip()

while not roll_no:
    print("Roll number cannot be empty.")
    roll_no = input("Enter roll number: ").strip()

subjects = [
    "Python Programming",
    "Mathematics",
    "Computer Science",
    "Statistics",
    "English"
]

marks = {}

for subject in subjects:
    while True:
        try:
            score = float(input("Enter marks in " + subject + " (out of 100): "))

            if 0 <= score <= 100:
                marks[subject] = score
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

total = sum(marks.values())
maximum = len(subjects) * 100
percentage = total / maximum * 100

failed_subjects = []

for subject, score in marks.items():
    if score < 40:
        failed_subjects.append(subject)

if failed_subjects:
    result = "FAIL"
else:
    result = "PASS"

if result == "FAIL":
    grade = "F"
elif percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "E"

print("\n" + "=" * 40)
print("          STUDENT REPORT")
print("=" * 40)

print("Name:", name)
print("Roll Number:", roll_no)
print("-" * 40)

for subject, score in marks.items():
    print(subject + ":", score, "/ 100")

print("-" * 40)
print("Total Marks:", total, "/", maximum)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Final Result:", result)

if failed_subjects:
    print("\nSubjects requiring improvement:")
    for subject in failed_subjects:
        print("-", subject)

print("=" * 40)
print("       END OF RESULT REPORT")
print("=" * 40)
