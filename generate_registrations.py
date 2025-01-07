import csv
import random
from faker import Faker

fake = Faker()

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

# Generate registrations for each student
registrations = []
for student in students:
    student_id = student['student_ID']
    student_name = student['student_name']
    for unit_id in random.sample(units, 3):  # Each student registers for 3 random units
        registration_id = f"REG{len(registrations) + 1:04d}"  # Unique registration ID
        registration_date = fake.date_between(start_date='-3y', end_date='today')  # Random registration date
        
        registrations.append([registration_id, student_id, student_name, unit_id, registration_date])

# Write to CSV file
with open('Data/student_unit_registration.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['registration_ID', 'student_ID', 'student_name', 'unit_ID', 'registration_date'])  # Header
    writer.writerows(registrations)  # Data

print("CSV file 'student_unit_registration.csv' created with registration records.")