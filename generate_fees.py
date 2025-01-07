import csv
import random

# Read students.csv to get the list of students
students = []
with open('Data/students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            'student_ID': row['student_ID'],
            'student_name': row['student_name'],  # Extract student names
            'course_ID': row['course_ID']  # Extract course IDs for each student
        })

# Read semesters.csv to get the list of semesters
semesters = []
with open('Data/semesters.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        semesters.append(row['semester_ID'])  # Extract semester IDs

# Generate fees for each student
fees = []
for i, student in enumerate(students):
    fees_id = f"FEE{i + 1:04d}"  # Unique fees ID
    student_id = student['student_ID']  # Student ID
    student_name = student['student_name']  # Student name
    course_id = student['course_ID']  # Course ID from students.csv
    semester_id = random.choice(semesters)  # Random semester ID
    fees_charged = round(random.uniform(50000, 100000), 2)  # Random fees charged
    fees_paid = round(random.uniform(0, fees_charged), 2)  # Random fees paid
    
    fees.append([fees_id, student_id, student_name, course_id, semester_id, fees_charged, fees_paid])

# Write to CSV file
with open('Data/fees.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['fees_ID', 'student_ID', 'student_name', 'course_ID', 'semester_ID', 'fees_charged', 'fees_paid'])  # Header
    writer.writerows(fees)  # Data

print("CSV file 'fees.csv' created with fees records.")