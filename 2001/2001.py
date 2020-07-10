import random

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
    for _ in range(2):
        dice_value = random.randint(1, 6)
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
        input("Let's roll!!!")
        computer = multi(computer)
        player = multi(player)
        print(f"Twoje punkty {player}")
        print(f"Computer punkty: {computer}")
    if player > computer:
        print("Wygrales!")
    else:
        print("Wygral computer!")


print(main())
