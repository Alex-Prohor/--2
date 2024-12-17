import doctest

class Aquarium:
    def __init__(self, capacity: float, current_water: float, fish_count: int):
        """
        Создание и подготовка объекта "Аквариум"

        :param capacity: Объём аквариума
        :param current_water: Текущее количество воды в литрах
        :param fish_count: Текущее количество рыб

        Примеры:
        >>> aquarium = Aquarium(100, 50, 5)
        """
        if capacity <= 0:
            raise ValueError("Объем аквариума должен быть положительным числом")
        if current_water < 0 or current_water > capacity:
            raise ValueError("Текущая вода должна быть в пределах объема аквариума")
        if fish_count < 0:
            raise ValueError("Количество рыб не может быть отрицательным")

        self.capacity = capacity
        self.current_water = current_water
        self.fish_count = fish_count

    def add_water(self, volume: float) -> None:
        """
        Добавляет воду в аквариум.

        :param volume: Объём добавляемой воды
        :raise ValueError: Если объём превышает вместимость аквариума.

        Примеры:
        >>> aquarium = Aquarium(100, 50, 5)
        >>> aquarium.add_water(30)
        >>> aquarium.current_water
        80
        """
        if volume < 0:
            raise ValueError("Добавляемый объём воды должен быть положительным числом")
        if self.current_water + volume > self.capacity:
            raise ValueError("Добавляемый объём превышает вместимость аквариума")
        self.current_water += volume

    def add_fish(self, count: int) -> None:
        """
        Добавляет рыб в аквариум.

        :param count: Количество добавляемых рыб
        :raise ValueError: Если количество добавляемых рыб отрицательное.

        Примеры:
        >>> aquarium = Aquarium(100, 50, 5)
        >>> aquarium.add_fish(3)
        >>> aquarium.fish_count
        8
        """
        if count < 0:
            raise ValueError("Количество добавляемых рыб не может быть отрицательным")
        self.fish_count += count

    def check_fish(self) -> int:
        """
        Возвращает текущее количество рыб в аквариуме.

        :return: Количество рыб

        Примеры:
        >>> aquarium = Aquarium(100, 50, 5)
        >>> aquarium.check_fish()
        5
        """
        return self.fish_count


if __name__ == "__main__":
    doctest.testmod()

    if __name__ == "__main__":
        aquarium = Aquarium(100, 50, 5)  # Инициализация аквариума с объёмом 100 литров, 50 литрами воды и 5 рыбами

        # Проверяем текущий уровень воды и количество рыб
        print("Текущий уровень воды в аквариуме:", aquarium.current_water)  # Ожидаем 50
        print("Текущее количество рыб в аквариуме:", aquarium.check_fish())  # Ожидаем 5

        # Добавляем 30 литров воды
        aquarium.add_water(30)
        print("После добавления воды, текущий уровень воды:", aquarium.current_water)  # Ожидаем 80

        # Добавляем 3 рыб в аквариум
        aquarium.add_fish(3)
        print("После добавления рыб, текущее количество рыб:", aquarium.check_fish())  # Ожидаем 8

        # Добавляем ещё 20 литров воды, чтобы довести до максимального объёма
        aquarium.add_water(20)
        print("Текущий уровень воды после полного заполнения:", aquarium.current_water)  # Ожидаем 100

        # Проверяем попытку добавить лишнюю воду (будет ошибка)
        try:
            aquarium.add_water(5)
        except ValueError as e:
            print("Ошибка:", e)  # Ожидаем сообщение о переполнении аквариума