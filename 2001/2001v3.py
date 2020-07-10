import random

def dice_type(code):
    possible_dices = ("D3", "D4", "D6", "D8", "D12", "D20", "D100")
    for i in possible_dices:
        if i in code:
            prefix, sufix = code.split(i)
            return prefix, i, sufix


def multi(score):
    roll = roll_dice()
    if roll == 7:
        return score // 7
    elif roll == 11:
        return score * 11
    else:
        return score + roll


def roll_dice():
    result = []
    print("Podaj kod kosci jaka chcesz rzucic xDy")
    data = input("Mozliwe kosci to: D3, D4, D6, D12, D20, D100 ")
    try:
        n = int(dice_type(data)[1][1:])
    except TypeError:
        return "Zly kod kosci"
    try:
        x = int(dice_type(data)[0])
    except ValueError:
        return "Zła wartosc x"
    for _ in range(x):
        dice_value = random.randint(1, n)
        result.append(dice_value)
    print(result)
    return sum(result)


def multi_computer(score):
    roll = roll_dice_computer()
    if roll == 7:
        return score // 7
    elif roll == 11:
        return score * 11
    else:
        return score + roll


def roll_dice_computer():
    result = []
    lista = [3, 4, 6, 8, 12, 20, 100]
    n = random.choice(lista)
    x = random.randint(1, 5)
    for _ in range(x):
        dice_value = random.randint(1, n)
        result.append(dice_value)
    print(result)
    return sum(result)


def main():
    player = 0
    computer = 0
    input("Witam w grze 2001, zaczynamy?")
    player += roll_dice()
    computer += roll_dice()
    while player < 201 and computer < 201:
        print(f"Twoje punkty {player}")
        print("Gracz")
        player = multi(player)
        print(f"Computer punkty: {computer}")
        print("Komputer")
        computer = multi_computer(computer)
    print(f"Twoje punkty {player}")
    print(f"Computer punkty: {computer}")
    if player > computer:
        print("Wygrales!")
    else:
        print("Wygral computer!")


print(main())
