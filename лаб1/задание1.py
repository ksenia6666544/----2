# TODO: Подробно описать три произвольных класса
from typing import Union

if __name__ == "__main__":
    import doctest


class Character:
    def __init__(self, name: str, age: int, strength: int | float):
        """
        Создание и подготовка к работе объекта "Персонаж"
        :param name: Имя персонажа
        :param age: Возраст персонажа (целое положительное число)
        :param strength: Базовая сила персонажа (число)

        Пример:
        >>> character_1 = Character("Mel", 33, 100)
        """
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = age

        if not isinstance(strength, (int, float)):
            raise TypeError("Сила персонажа должна быть числом")
        self.strength = strength

    def is_child(self) -> bool:
        """
        Функция проверяет является ли персонаж ребенком (младше 18 лет)
        :return: True если персонаж ребенок, иначе False

        Пример:
        >>> character_1 = Character("Mel", 33, 100)
        >>> character_1.is_child()
        False
        """
        return self.age < 18

    def years_passed(self, count: int) -> None:
        """
        Увеличивает возраст персонажа на указанное количество лет
        :param count: Количество лет, которое прошло
        :raise TypeError: Если count не целое число
        :raise ValueError: Если count отрицательное

        Пример:
        >>> character_1 = Character("Mel", 33, 100)
        >>> character_1.years_passed(5)
        """
        if not isinstance(count, int):
            raise TypeError("Количество лет должно быть целым числом")
        if count < 0:
            raise ValueError("Количество лет не может быть отрицательным")
        self.age += count


class Wizard:
    def __init__(self, hp: int, armor: int):
        """
        Создание объекта "Волшебник"
        :param hp: Здоровье волшебника (1-100)
        :param armor: Броня (неотрицательное число). Блокирует 1/3 урона.

        Пример:
        >>> wizard_1 = Wizard(100, 15)
        """
        if not isinstance(hp, int):
            raise TypeError("HP должно быть целым числом")
        if not (0 < hp <= 100):
            raise ValueError("HP должно быть в диапазоне от 1 до 100")
        self.hp = hp

        if not isinstance(armor, int):
            raise TypeError("Броня должна быть целым числом")
        if armor < 0:
            raise ValueError("Броня не может быть отрицательной")
        self.armor = armor

    def is_hit(self, impact: int) -> None:
        """
        Обрабатывает удар по волшебнику с учетом брони
        :param impact: Наносимый урон (неотрицательное число)
        :raise TypeError: Если урон не целое число
        :raise ValueError: Если урон отрицательный

        Пример:
        >>> wizard_1 = Wizard(100, 15)
        >>> wizard_1.is_hit(30)
        """
        if not isinstance(impact, int):
            raise TypeError("Урон должен быть целым числом")
        if impact < 0:
            raise ValueError("Урон не может быть отрицательным")

        damage = max(0, impact - self.armor // 3)
        self.hp = max(0, self.hp - damage)

    def is_dead(self) -> bool:
        """
        Проверяет, мертв ли волшебник
        :return: True если HP <= 0, иначе False

        Пример:
        >>> wizard_1 = Wizard(100, 15)
        >>> wizard_1.is_dead()
        False
        """
        return self.hp <= 0


class Ghost:
    def __init__(self, place: str, rank: int):
        """
        Создание объекта "Призрак"
        :param place: Место нахождения ("Earth" или "spirit world")
        :param rank: Ранг призрака (1-100)

        Пример:
        >>> ghost_1 = Ghost("Earth", 15)
        """
        if place not in ("Earth", "spirit world"):
            raise ValueError("Место должно быть 'Earth' или 'spirit world'")
        self.place = place

        if not isinstance(rank, int):
            raise TypeError("Ранг должен быть целым числом")
        if not (0 < rank <= 100):
            raise ValueError("Ранг должен быть в диапазоне от 1 до 100")
        self.rank = rank

    def the_level(self) -> str:
        """
        Определяет уровень крутости призрака
        :return: "призрак слаб" если ранг <=80, иначе "этот призрак супер крут"

        Пример:
        >>> ghost_1 = Ghost("Earth", 15)
        >>> ghost_1.the_level()
        'призрак слаб'
        """
        return "призрак слаб" if self.rank <= 80 else "этот призрак супер крут"

    def is_boosted(self, add: int) -> None:
        """
        Увеличивает ранг призрака
        :param add: Значение для увеличения ранга
        :raise TypeError: Если add не целое число
        :raise ValueError: Если новый ранг выйдет за пределы 1-100

        Пример:
        >>> ghost_1 = Ghost("Earth", 15)
        >>> ghost_1.is_boosted(5)
        """
        if not isinstance(add, int):
            raise TypeError("Добавка к рангу должна быть целым числом")

        new_rank = self.rank + add
        if not (0 < new_rank <= 100):
            raise ValueError("Ранг должен оставаться в диапазоне от 1 до 100")
        self.rank = new_rank


if __name__ == "__main__":
    doctest.testmod()