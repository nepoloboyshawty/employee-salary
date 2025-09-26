from modules.classes import *

employees = [
    Manager("Андрей", 130000),
    Developer("Егор", 234000, 2),
    Trainee("Кирилл", 67000)
]

for employee in employees:
    print(employee)