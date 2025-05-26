from task_1 import Сharacter, Wizard, Ghost

if __name__ == "__main__":
    character_1 = Сharacter("Mel", 33, 100)
    wizard_1 = Wizard(100, 15)
    ghost_1 = Ghost("Earth", 15)


    try:
        character_1.years_passed('5')
        print(character_1.age)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        wizard_1.is_hit('30')
        print(wizard_1.hp)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        ghost_1.is_boosted('5')
        print(ghost_1.rang)
    except TypeError:
        print('Ошибка: неправильные данные')


