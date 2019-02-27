import csv

with open("student_list.csv","r") as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line[0])