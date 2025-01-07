import csv
import random
from faker import Faker

fake = Faker()

# Define course IDs
course_ids = ['CS001', 'IT001', 'SE001', 'BCT2101', 'PMI2203', 'AFT2202']

# Define genders
genders = ['Male', 'Female', 'Other']

# Generate 1,000 student records
students = []
for i in range(1, 1001):
    year = random.choice([2021, 2022, 2023, 2024])  # Random year for the batch
    student_id = f"SCT211-{i:04d}/{year}"  # Unique student ID with year
    student_name = fake.name()  # Random name
    gender = random.choice(genders)  # Random gender
    enrollment_date = fake.date_between(start_date=f'-{2024 - year}y', end_date='today')  # Enrollment date based on year
    course_id = random.choice(course_ids)  # Random course ID
    
    students.append([student_id, student_name, gender, enrollment_date, course_id])

# Write to CSV file
with open('Data/students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['student_ID', 'student_name', 'gender', 'enrollment_date', 'course_ID'])  # Header
    writer.writerows(students)  # Data

print("CSV file 'students.csv' created with 1,000 student records.")