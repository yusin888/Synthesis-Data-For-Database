import csv
import random

# Define semester data
semesters = []
semester_numbers = [1, 2, 3]
years = [2021, 2022, 2023, 2024]
course_ids = ['CS001', 'IT001', 'SE001']

for i in range(1, 1001):
    semester_id = f"SEM{i:04d}"  # Unique semester ID
    semester_number = random.choice(semester_numbers)  # Random semester number
    year = random.choice(years)  # Random year
    course_id = random.choice(course_ids)  # Random course ID
    
    semesters.append([semester_id, semester_number, year, course_id])

# Write to CSV file
with open('semesters.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['semester_ID', 'semester_number', 'year', 'course_ID'])  # Header
    writer.writerows(semesters)  # Data

print("CSV file 'semesters.csv' created with semester records.")