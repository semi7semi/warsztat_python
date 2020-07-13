import random


def multi(score):
    """funkcja modyfikuje wynik przy rzucie 7 i 11"""
    roll = roll_dice()
    if roll == 7:
        return score // 7
    elif roll == 11:
        return score * 11
    else:
        return score + roll


def multi_computer(score):
    """funkcja modyfikuje wynik przy rzucie 7 i 11 dla komputera"""
    roll = roll_dice_computer()
    if roll == 7:
        return score // 7
    elif roll == 11:
        return score * 11
    else:
        return score + roll


def roll_dice_computer():
    """symulacja rzutu kostkami D6 oraz zsumowanie wyniku dla komputera
    losowa ilosc kosci"""
    result = []
    x = random.randint(1, 4)
    for _ in range(x):
        dice_value = random.randint(1, 6)
        result.append(dice_value)
    print(result)
    return sum(result)


def roll_dice():
    """symulacja rzutu kostkami D6 oraz zsumowanie wyniku"""
    result = []
    x = int(input("Iloma koscmi chcesz rzucic? "))
    if x > 5 or x < 1:
        return "mozesz wybrac tylko 1 - 4 kosci"
    else:
        for _ in range(x):
            dice_value = random.randint(1, 6)
            result.append(dice_value)
        print(result)
        return sum(result)


def main():
    """glowna funkcja,
    porownuje symulacje rzutow dla komputera i gracza,
    kto pierwszy spelni warunki wygrywa."""
    player = 0
    computer = 0
    input("Witam w grze 2001, zaczynamy?")
    player += roll_dice()
    computer += roll_dice_computer()
    while player < 2001 and computer < 2001:
        player = multi(player)
        print(f"Twoje punkty {player}")
        computer = multi_computer(computer)
        print(f"Computer punkty: {computer}")
    if player > computer:
        print("Wygrales!")
    else:
        print("Wygral computer!")


print(main())
