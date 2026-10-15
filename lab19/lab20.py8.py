#student course enrollment analysis
python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
#convert lists to sets to remove duplicates
python_students = set(python_class)
java_students = set(java_class)
## Students taking both courses
both_courses = python_students & java_students

# Students taking only Python
only_python = python_students - java_students

# Students taking exactly one course
exactly_one = python_students ^ java_students

# Every unique student in sorted order
all_students = sorted(python_students | java_students)
print("Students taking both courses:", sorted(both_courses))
print("Students taking only Python:", sorted(only_python))
print("Students taking exactly one course:", sorted(exactly_one))
print("All unique students:", all_students)

# Ask for a student's name
name = input("\nEnter a student's name: ").strip().title()

# Check course enrollment
if name in python_students and name in java_students:
    print(name, "is enrolled in both Python and Java.")
elif name in python_students:
    print(name, "is enrolled in Python only.")
elif name in java_students:
    print(name, "is enrolled in Java only.")
else:
    print(name, "is not enrolled in either course.")