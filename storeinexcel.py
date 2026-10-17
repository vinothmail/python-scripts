import csv
import os

print("Enter a string: ")   
str1 = input()
csv_file = "test.csv"   # fixed file name

# Check if file already exists
file_exists = os.path.isfile(csv_file)

with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)
    
    # Write header only if file is new
    if not file_exists:
        writer.writerow(["Original String", "Length", "Reversed", "Uppercase", "Lowercase"])
    
    # Append new row
    writer.writerow([str1, len(str1), str1[::-1], str1.upper(), str1.lower()])
