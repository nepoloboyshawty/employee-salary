from abc import ABC, abstractmethod

class Employee(ABC):
    """
    Данный класс является родительским для классов,
    созданных ниже.

    Attributes:
        name (str): Имя сотрудника.
        base_salary (float): Базовая зарплата сотрудника.

    Raises:
        ValueError для name: Если переданное имя не является
            строкой или имеет длину меньше одного.
        ValueError для base_salary: Если зарплата не указана
            целочисленным или дробным значением или является
            отрицательной.
    """
    name: str
    base_salary: str

    def __init__(self, name: str, base_salary: float):
        """
        Инициализирует объект Employee.

        Args:
            name (str): Имя сотрудника.
            base_salary (float): Базовая зарплата сотрудника.
        """
        if not name or not isinstance(name, str):
            raise ValueError("Имя должно состоять из букв")
        elif not isinstance(base_salary, (float, int)):
            raise ValueError("Зарплата должна быть указана целочисленным или дробным значением")
        elif base_salary < 0:
            raise ValueError("Зарпалата не может быть отрицательной")

        self.__name = name
        self.__base_salary = base_salary

    @property
    def salary(self):
        """
        Возвращает инициализированную зарплату сотрудника.

        Returns:
            float: Инициализированная зарплата.
        """
        return self.__base_salary

    @property
    @abstractmethod
    def calculate_salary(self):
        """
        Создание абстрактного метода для дальнейшего
        использования в дочерних классах.
        """
        pass

    def __str__(self):
        """
        Возвращает информацию о сотруднике в виде строки.

        Returns:
            str: Информация о сотруднике.
        """
        return f"Имя: {self.__name} | Должность: {self.__class__.__name__} | Зарплата: {self.calculate_salary}"


class Manager(Employee):
    """
    Данный класс создает информацию о сотруднике
    с должностью Менеджер.
    """
    @property
    def calculate_salary(self):
        """
        Возвращает зарплату сотрудника с надбавкой +20%
        от всей базовой.

        Returns:
            float: Повышенная зарплата сотрудника.
        """
        return self.salary + (self.salary * 0.2)


class Developer(Employee):
    """
    Данный класс создает информацию о сотруднике
    с должностью Разработчик.

    Attributes:
        name (str): Имя сотрудника.
        base_salary (float): Базовая зарплата сотрудника.
        projects_completed (int): Завершенные проекты.

    Raises:
        ValueError: Если количество проектов указано не
            целочисленным значением.
    """
    projects_completed: int

    def __init__(self, name: str, base_salary: float, projects_completed: int):
        """
        Дополнительная инициализация объекта.

        Args:
            name (str): Имя сотрудника.
            base_salary (float): Базовая зарплата сотрудника.
            projects_completed (int): Количество завершенных проектов.
        """
        super().__init__(name, base_salary)

        if not isinstance(projects_completed, int):
            raise ValueError("Количество проектов должно быть указано целочисленным значением")

        self.__projects_completed = projects_completed

    @property
    def calculate_salary(self):
        """
        Возвращает зарплату сотрудника с надбавкой +10%
        от всей базовой и добавляет 1000 за каждый завершенный проект.

        Returns:
            float: Повышенная зарплата сотрудника.
        """
        return self.salary + (self.salary * 0.1) + (1000 * self.__projects_completed)


class Intern(Employee):
    """
    Данный класс создает информацию о сотруднике
    с должностью Интерн.
    """
    @property
    def calculate_salary(self):
        """
        Возвращает половину зарплаты сотрудника от всей базовой.

        Returns:
            float: Урезанная зарплата сотрудника.
        """
        return self.salary / 2