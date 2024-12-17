import doctest

class Backpack:
    def __init__(self, capacity: float, current_load: float):
        """
        Создание и подготовка объекта "Рюкзак"

        :param capacity: Максимальный объём рюкзака
        :param current_load: Текущий объём загруженных предметов

        Примеры:
        >>> backpack = Backpack(30, 10)  # Инициализация рюкзака
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Объем рюкзака должен быть числом (int или float)")
        if capacity <= 0:
            raise ValueError("Объем рюкзака должен быть положительным числом")

        if not isinstance(current_load, (int, float)):
            raise TypeError("Текущая нагрузка должна быть числом (int или float)")
        if current_load < 0 or current_load > capacity:
            raise ValueError("Нагрузка должна быть неотрицательной и не превышать объём рюкзака")

        self.capacity = capacity
        self.current_load = current_load

    def is_backpack_empty(self) -> bool:
        """
        Проверяет, пуст ли рюкзак.

        :return: Возвращает True, если рюкзак пуст.

        Примеры:
        >>> backpack = Backpack(30, 0)
        >>> backpack.is_backpack_empty()
        True
        """
        return self.current_load == 0

    def add_items(self, load: float) -> None:
        """
        Добавляет нагрузку в рюкзак.

        :param load: Объём добавляемых предметов
        :raise ValueError: Если добавляемая нагрузка превышает доступное место в рюкзаке.

        Примеры:
        >>> backpack = Backpack(30, 10)
        >>> backpack.add_items(15)
        >>> backpack.current_load
        25
        """
        if load < 0:
            raise ValueError("Добавляемая нагрузка должна быть положительной")
        if self.current_load + load > self.capacity:
            raise ValueError("Добавляемая нагрузка превышает вместимость рюкзака")
        self.current_load += load

    def remove_items(self, load: float) -> None:
        """
        Удаляет предметы из рюкзака.

        :param load: Объём удаляемых предметов
        :raise ValueError: Если удаляемая нагрузка больше текущей загрузки.

        Примеры:
        >>> backpack = Backpack(30, 10)
        >>> backpack.remove_items(5)
        >>> backpack.current_load
        5
        """
        if load < 0:
            raise ValueError("Удаляемая нагрузка должна быть положительной")
        if load > self.current_load:
            raise ValueError("Удаляемая нагрузка больше текущей")
        self.current_load -= load


if __name__ == "__main__":
    doctest.testmod()

    if __name__ == "__main__":
        tank = Backpack(30, 10)

        # Проверяем, пуст ли рюкзак
        print("Рюкзак пустой?", tank.is_backpack_empty())  # Ожидаем False

        # Добавляем 10 литров
        tank.add_items(20)
        print("Текущий объем рюкзака:", tank.current_load)  # Ожидаем 30

        # Используем 5 литров
        tank.remove_items(5)
        print("Остаток места:", tank.current_load)  # Ожидаем 25