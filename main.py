class Animals:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self._sage = age / 2

    @staticmethod
    def animal_sound():
        return "Нет звука"


class Dog(Animals):
    @property
    def info(self):
        return f"{self.name}, {self.age}, {self._sage}"

    @staticmethod
    def animal_sound():
        return "Гав-гав"


dog = Dog("Гавс", 4)
print(dog.info, dog.animal_sound())