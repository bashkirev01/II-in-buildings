class Vehicle:
    """
    Базовый класс для представления транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def info(self) -> str:
        """
        Возвращает информацию о транспортном средстве.

        :return: Информация о марке, модели и годе выпуска.
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __str__(self) -> str:
        """
        Строковое представление транспортного средства.

        :return: Строка с информацией о транспортном средстве.
        """
        return f"Vehicle(Brand: {self.brand}, Model: {self.model}, Year: {self.year})"

    def __repr__(self) -> str:
        """
        Представление транспортного средства для отладки.

        :return: Информация о транспортном средстве.
        """
        return f"Vehicle(brand='{self.brand}', model='{self.model}', year={self.year})"


class Car(Vehicle):
    """
    Класс, представляющий легковой автомобиль, наследующий от Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        """
        Инициализация легкового автомобиля.

        :param brand: Марка легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param doors: Количество дверей в легковом автомобиле.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self.__doors = doors  # Приватный атрибут, так как количество дверей не должно изменяться после создания

    def info(self) -> str:
        """
        Возвращает информацию о легковом автомобиле, включая количество дверей.

        :return: Информация о легковом автомобиле.
        """
        base_info = super().info()  # Вызов метода базового класса
        return f"{base_info}, Doors: {self.__doors}"

    def __str__(self) -> str:
        """
        Строковое представление легкового автомобиля.

        :return: Строка с информацией о легковом автомобиле.
        """
        return f"Car(Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Doors: {self.__doors})"

    def __repr__(self) -> str:
        """
        Представление легкового автомобиля для отладки.

        :return: Информация о легковом автомобиле.
        """
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, doors={self.__doors})"


# Пример использования классов
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, 4)
    print(car)  # Придет вызов __str__
    print(repr(car))  # Придет вызов __repr__
    print(car.info())  # Информация о легковом автомобиле

