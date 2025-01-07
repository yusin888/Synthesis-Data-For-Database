import csv
import random
from faker import Faker

fake = Faker()

# Define course IDs
# CS001: Computer Science
# IT001: Information Technology
# SE001: Software Engineering
course_ids = ['CS001', 'IT001', 'SE001'] 

# Define genders
genders = ['Male', 'Female', 'Other']

# Generate 1,000 student records
students = []
for i in range(1, 1001):
    student_id = f"SCT211-{i:04d}/2021"  # Unique student ID
    student_name = fake.name()  # Random name
    gender = random.choice(genders)  # Random gender
    enrollment_date = fake.date_between(start_date='-3y', end_date='today')  # Random enrollment date
    course_id = random.choice(course_ids)  # Random course ID
    
    students.append([student_id, student_name, gender, enrollment_date, course_id])

# Write to CSV file
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['student_ID', 'student_name', 'gender', 'enrollment_date', 'course_ID'])  # Header
    writer.writerows(students)  # Data

print("CSV file 'students.csv' created with 1,000 student records.")