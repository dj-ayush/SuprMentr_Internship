# Student Data Manager

students = {}

# Input data for 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Find topper
topper = max(students, key=students.get)
top_marks = students[topper]

# Calculate class average
average = sum(students.values()) / len(students)

# Function to assign grades
def assign_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

print("\nStudent Grades:")
for name, marks in students.items():
    grade = assign_grade(marks)
    print(name, ":", marks, "Grade:", grade)

print("\nTopper:", topper, "-", top_marks)
print("Class Average:", average)