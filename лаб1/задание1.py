# TODO: Подробно описать три произвольных класса
from typing import Union

if __name__ == "__main__":
    import doctest


class Сharacter:

    def __init__(self, name: str, age: int, strength: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Персонаж"
        :param name: Имя
        :param age: возраст
        :param strength: базовый урон

        Пример:
        >>> character_1 = Сharacter("Mel", 33, 100)
        """
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст задается целым числом")
        if age <= 0:
            raise ValueError("Возраст задается целым положительным числом")
        self.age = age

        if not isinstance(strength, (int, float)):
            raise TypeError("Сила персонажа должна быть выражена числом")
        self.strength = strength

    def is_child(self) -> bool:
        """
        Функция проверяет является ли персонаж ребенком
        :return: Является ли персонаж ребенком

        Пример:
        >>> character_1 = Сharacter("Mel", 33, 100)
        >>> character_1.is_child()
        False
        """

        if self.age <= 18:
            return True
        else:
            return False

    def years_passed(self, count: int) -> None:
        """
       :param count: количество прошедших лет с обозначеного ранее года
       :raise: Сколько лет стало персонажу через это количество лет, как он повзрослел

       Пример:
       >>> character_1 = Сharacter("Mel", 33, 100)
       >>> character_1.years_passed(5)
       """
        if not isinstance(count, int):
            raise TypeError("Прошедшие года задаются целым числом")
        if count <= 0:
            raise ValueError("Прошедшие года задаются целым положительным числом")

        self.age = self.age + count


class Wizard:
    def __init__(self, hp: int, armor: int):
        """
        :param hp: Здоровье волшебника, пока оно больше нуля, он жив.
        :param armor: Броня. Блокирует 1/3 урона.

        Пример:
        >>> wizard_1 = Wizard(100, 15)
        """
        if not isinstance(hp, int):
            raise TypeError("HP задается целым числом")
        if not (0 < hp <= 100):
            raise ValueError("Значение HP находится в промежутке от 1 до 100 единиц")
        self.hp = hp

        if not isinstance(armor, int):
            raise TypeError("Коефицент брони задается целым числом")
        if 0 > armor:
            raise ValueError("Значение брони не может быть отрицительным")
        self.armor = armor

    def is_hit(self, impact: int) -> None:
        """
        :param impact: наносимый урон
        :reise: значение здоровья после удара, с учетом брони

        Пример:
        >>> wizard_1 = Wizard(100, 15)
        >>> wizard_1.is_hit(30)
        """
        if not isinstance(impact, int):
            raise TypeError("Урон задается целым числом")
        if 0 > impact:
            raise ValueError("Значение Уронa не может быть отрицительным")

        if (impact - self.armor / 3) < 0:
            self.hp -= 0
        elif 0 < (impact - self.armor / 3) < self.hp:
            self.hp -= (impact - self.armor / 3)
        else:
            self.hp = 0

    def is_dead(self) -> bool:
        """
        Функция проверяет живо ли приведение
        :return: его статус. мертв ли.
        Пример:
        >>> wizard_1 = Wizard(100, 15)
        >>> wizard_1.is_dead()
        False
        """
        if self.hp <= 0:
            return True
        else:
            return False


class Ghost:
    def __init__(self, place: str, rang: int):
        """
        увеличение уровня
        :param place: где сейчас призрак
        :param rang: крутизна призрака

        Пример:
        >>> ghost_1 = Ghost("Earth", 15)
        """
        if place != "Earth" and place != "spirit world":
            raise ValueError("Where is your Ghost! (Earth/spirit world)")
        self.place = place

        if not isinstance(rang, int):
            raise TypeError("Ранг задается целым числом")
        if not (0 < rang <= 100):
            raise ValueError("Значение ранга находится в промежутке от 1 до 100 единиц")
        self.rang = rang

    def the_level(self) -> str:
        """
        Фурнкция возвращает уровень крутости призрака
        1-80 слабый
        81-100 супер крутой
        :return: уровень крутости призрака

        Пример:
        >>> ghost_1 = Ghost("Earth", 15)
        >>> ghost_1.the_level()
        'призрак слаб'
        """
        if self.rang <= 80:
            return "призрак слаб"
        else:
            return "этот призрак супер крут"

    def is_boosted(self, add: int) -> None:
        """
        улучшение
        :param add: добавка к рангу
        :raise: ранг

        >>> ghost_1 = Ghost("Earth", 15)
        >>> ghost_1.is_boosted(5)
        """
        if not isinstance(add, int):
            raise TypeError("Этот параметр задается целым числом")

        if (0 > add) and (add + self.rang >= 100):
            raise ValueError("Значение ранга находится в промежутке от 1 до 100 единиц")
        self.rang += add

if __name__ == "__main__":
    doctest.testmod()