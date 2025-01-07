import csv

# Define unit data
units = [
    ['UNIT001', 'ICS2101', 'Introduction to Computer Science', 'CS001'],
    ['UNIT002', 'ICS2202', 'Data Structures and Algorithms', 'CS001'],
    ['UNIT003', 'BCT2103', 'Introduction to IT', 'IT001'],
    ['UNIT004', 'BCT2201', 'Networking Basics', 'IT001'],
    ['UNIT005', 'ICS2301', 'Software Design', 'SE001'],
    ['UNIT006', 'ICS2302', 'Software Testing', 'SE001']
]

# Write to CSV file
with open('Data/units.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['unit_ID', 'unit_code', 'unit_name', 'course_ID'])  # Header
    writer.writerows(units)  # Data

print("CSV file 'units.csv' created with unit records.")