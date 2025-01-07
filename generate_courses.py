import csv

# Define course data
courses = [
    ['CS001', 'Computer Science'],
    ['IT001', 'Information Technology'],
    ['SE001', 'Software Engineering']
]

# Write to CSV file
with open('courses.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['course_ID', 'course_name'])  # Header
    writer.writerows(courses)  # Data

print("CSV file 'courses.csv' created with course records.")