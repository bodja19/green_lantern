import csv

with open('users', 'r') as f:
    reader = csv.DictReader(f)
    users = [i for i in reader]
