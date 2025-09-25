from modules.classes import *

employees = [
    Manager("Елена", 24244),
    Developer("Виталий", 2, 3),
    Intern("Александр", 70000)
]

for emp in employees:
    print(emp)