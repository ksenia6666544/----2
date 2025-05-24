class Evergreen:
    """
    Базовый класс для хвойных деревьев

    Attributes:
        crown (str): Вид кроны дерева (например, овальная, конусообразная)
        cone (str): Вид шишки дерева (например, удлиненная, округлая)
        tone (str): Цвет (оттенок) хвои (например, тёмный, светлый)
    """

    def __init__(self, crown: str, cone: str, tone: str):
        self._crown = crown
        self._cone = cone
        self._tone = tone

    @property
    def crown(self) -> str:
        return self._crown

    @property
    def cone(self) -> str:
        return self._cone

    @property
    def tone(self) -> str:
        return self._tone

    def __str__(self) -> str:
        return f"{self.crown} {self.cone} {self.tone}"

    def __repr__(self) -> str:
        return f"Evergreen(crown={self.crown!r}, cone={self.cone!r}, tone={self.tone!r})"


class Pine(Evergreen):
    """
    Дочерний класс для сосны

    Attributes:
        crown (str): Вид кроны дерева (унаследовано)
        cone (str): Вид шишки дерева (унаследовано)
        tone (str): Цвет (оттенок) хвои (унаследовано)
        height (float): Высота дерева
    """

    def __init__(self, crown: str, cone: str, tone: str, height: float):
        super().__init__(crown, cone, tone)
        self.height = height

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError('Высота дерева должна быть числовой')
        if value <= 0:
            raise ValueError('Высота дерева должна быть положительной')
        self._height = value

    def __str__(self) -> str:
        return f"{self.crown} {self.cone} {self.tone}. Высота: {self.height:.2f} м"

    def __repr__(self) -> str:
        return f"Pine(crown={self.crown!r}, cone={self.cone!r}, tone={self.tone!r}, height={self.height:.2f})"

    def cut_down_tree(self) -> str:
        """
        Метод для обозначения процесса рубки дерева.

        Returns:
            str: Сообщение о том, что дерево было срублено.
        """
        return "Дерево срублено"

    def plant_tree(self) -> str:
        """
        Метод для обозначения посадки дерева.

        Returns:
            str: Сообщение о посадке дерева.
        """
        return "Дерево посажено"

    def decorate_tree(self) -> str:
        """
        Метод для украшения дерева.

        Returns:
            str: Сообщение о украшении дерева.
        """
        return "Дерево украшено"
