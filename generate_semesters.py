import csv
import random

# Read students.csv to get the list of students
students = []
with open('Data/students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            'student_ID': row['student_ID'],
            'year': int(row['student_ID'].split('/')[1])  # Extract year from student_ID
        })

# Define semester data
semesters = []
semester_numbers = [1, 2, 3]

for i, student in enumerate(students):
    semester_id = f"SEM{i + 1:04d}"  # Unique semester ID
    semester_number = random.choice(semester_numbers)  # Random semester number
    year = student['year']  # Year from student_ID
    course_id = random.choice(['CS001', 'IT001', 'SE001', 'BCT2101', 'PMI2203', 'AFT2202'])  # Random course ID
    
    semesters.append([semester_id, semester_number, year, course_id])

# Write to CSV file
with open('Data/semesters.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['semester_ID', 'semester_number', 'year', 'course_ID'])  # Header
    writer.writerows(semesters)  # Data

print("CSV file 'semesters.csv' created with semester records.")