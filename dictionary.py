import csv

filename ="testfile1.csv"

# opening the file using "with"
# statement
with open(filename, 'r') as data:
    for line in csv.DictReader(data):
        print(line["First_name"])
        print(line["Last_Name"])    
print(type(line))