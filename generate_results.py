import csv
import random

# Read students.csv to get the list of students
students = []
with open('Data/students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            'student_ID': row['student_ID'],
            'student_name': row['student_name']  # Extract student names
        })

# Read units.csv to get the list of units
units = []
with open('Data/units.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        units.append(row['unit_ID'])  # Extract unit IDs

# Generate results for each student
results = []
for student in students:
    student_id = student['student_ID']
    student_name = student['student_name']
    for unit_id in units:
        result_id = f"RES{len(results) + 1:04d}"  # Unique result ID
        marks = round(random.uniform(40, 100), 2)  # Random marks between 40 and 100
        grade = 'A' if marks >= 70 else 'B' if marks >= 60 else 'C' if marks >= 50 else 'D' if marks >= 40 else 'E'
        
        results.append([result_id, student_id, student_name, unit_id, marks, grade])

# Write to CSV file
with open('Data/results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['result_ID', 'student_ID', 'student_name', 'unit_ID', 'marks', 'grade'])  # Header
    writer.writerows(results)  # Data

print("CSV file 'results.csv' created with results records.")