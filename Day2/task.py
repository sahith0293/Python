# Storing Student Records using Lists & Tuples
students = [
    ("John", 101, [85, 90, 78], 90.0),  # Tuple: Immutable student info
    ("Alice", 102, [72, 88, 95], 85.0),
    ("Bob", 103, [60, 75, 70], 80.0)
]

# Function to Calculate Average Marks
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to Check Scholarship Eligibility using Boolean
def is_eligible_for_scholarship(avg_marks, attendance):
    return avg_marks > 80 and attendance > 85  # Boolean Logic

# Complex Numbers - Hypothetical Grade Adjustment
cmp1 = 2 + 3j  # Bonus grading complex number
cmp2 = 1 - 1j  # Deduction factor

print("Student Records:")
for student in students:
    name, roll, marks, attendance = student
    avg_marks = calculate_average(marks)

    # Complex Number Operation (Hypothetical Adjustment)
    grade_adjustment = cmp1 * cmp2  # Example of complex number operation

    print(f"\nStudent: {name} (Roll No: {roll})")
    print(f"Marks: {marks}")
    print(f"Average Marks: {avg_marks:.2f}")
    print(f"Attendance: {attendance}%")
    print(f"Scholarship Eligibility: {is_eligible_for_scholarship(avg_marks, attendance)}")
    print(f"Complex Grade Adjustment: {grade_adjustment}")

# List Slicing - Display Top Students
students_list = ["John", "Alice", "Bob", "Emma", "David"]
print("\nStudent List Slicing:")
print(students_list[1:4])   # Extracting a sublist
print(students_list[-3:])   # Extracting last three students
students_list[-1] = "Daniel"  # Modifying list
print("Updated List:", students_list)

# Tuple Operations
tup1 = (5, 10, 15, 20, 25)
print("\nTuple Slicing Examples:")
print(tup1[1:4])   # Extracting a sub-tuple
print(tup1[-1:-4:-1])  # Reverse slicing

# Using Range to Generate Student Roll Numbers
print("\nStudent Roll Numbers:")
print(list(range(101, 106)))   # Roll numbers from 101 to 105
print(list(range(200, 190, -2)))  # Even roll numbers in reverse

# Checking Boolean Conditions
print("\nBoolean Logic:")
print(2 < 3)   # True
print(2 >= 3)  # False

# Converting Boolean to Integer
print("\nBoolean to Integer Conversion:")
print(int(True))  # Output: 1
print(int(False)) # Output: 0

# String Mutability Test (Strings are Immutable)
s = "hello"
# s[0] = "H"  # Uncommenting this line will give a TypeError: Strings are immutable
s = "Hello World"  # Creates a new string object instead of modifying the old one
print("\nModified String:", s)  # New string object created

# Using Complex Number Operations
cmp3 = cmp1 + cmp2
print("\nComplex Number Operations:")
print(cmp3)
print(cmp1 - cmp2)
print(cmp1 * cmp2)
print(cmp1 / cmp2)
print(cmp1 ** cmp2)  # Exponentiation of complex numbers