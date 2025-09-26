from unittest import TestCase, main
from modules.classes import Manager, Developer, Trainee

class TestClasses(TestCase):
    def test_manager(self):
        managers = [
            Manager("Елена", 140000),
            Manager("Артемий", 123300),
            Manager("Валерия", 134400)
        ]

        self.assertEqual(str(managers[0]), "Имя: Елена | Должность: Manager | Зарплата: 168000.0")
        self.assertEqual(str(managers[1]), "Имя: Артемий | Должность: Manager | Зарплата: 147960.0")
        self.assertEqual(str(managers[2]), "Имя: Валерия | Должность: Manager | Зарплата: 161280.0")

    def test_developer(self):
        developers = [
            Developer("Александр", 270000, 4),
            Developer("Михаил", 187000, 1),
            Developer("Владимир", 153353, 0)
        ]

        self.assertEqual(str(developers[0]), "Имя: Александр | Должность: Developer | Зарплата: 301000.0")
        self.assertEqual(str(developers[1]), "Имя: Михаил | Должность: Developer | Зарплата: 206700.0")
        self.assertEqual(str(developers[2]), "Имя: Владимир | Должность: Developer | Зарплата: 168688.3")

    def test_trainee(self):
        trainees = [
            Trainee("Олег", 70000),
            Trainee("Петр", 85000),
            Trainee("Иван", 59999)
        ]

        self.assertEqual(str(trainees[0]), "Имя: Олег | Должность: Trainee | Зарплата: 35000.0")
        self.assertEqual(str(trainees[1]), "Имя: Петр | Должность: Trainee | Зарплата: 42500.0")
        self.assertEqual(str(trainees[2]), "Имя: Иван | Должность: Trainee | Зарплата: 29999.5")


if __name__ == "__main__":
    main()
