import random

print("""
    Witaj w grze LOTTO! 
    Wytypuj 6 liczb od 1 do 49 a twoje marzenia sie spelnia!
""")


def lotto():
    n = 1
    score = 0
    tab = []
    computer_no = list(range(1, 50))
    random.shuffle(computer_no)
    while n != 7:
        try:
            player_no = int(input(f"Podaj liczbe {n}: "))
            if player_no <=0 or player_no >= 50:
                print("Podaj liczbe z przedziału 1-49")
            elif player_no in tab:
                print("Podales juz ta liczbe")
            else:
                tab.append(player_no)
                n += 1
            tab.sort()
        except ValueError:
            print("-----podaj liczbe!-----")
    print(f"Twoje numerki: {tab}")
    for i in range(5):
        if tab[i] in computer_no[:6]:
            score += 1
    print(f"Szczesliwe numerki: {computer_no[:6]}")
    return f"Trafiles {score} raz/y"


print(lotto())
