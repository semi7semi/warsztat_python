import random

print("""
    Witaj w grze LOTTO! 
    Wytypuj 6 liczb od 1 do 49 a twoje marzenia sie spelnia!
""")


def ask(question):
    """zadaje pytanie o 6 liczb gracza"""
    answer = None
    while answer not in range(1, 50):
        try:
            answer = int(input(question))
        except ValueError:
            print("Podaj liczbe z przedzialu 1-49")

    return answer


def lotto():
    """Program losuje 6 wartosci z przedzialu 1 - 49 i
    porownuje je z wartosciami podanymi przez gracza"""
    n = 1
    score = 0
    tab = []
    computer_no = list(range(1, 50))
    random.shuffle(computer_no)
    while n != 7:
        player_no = ask(f"Podaj liczbe {n}, (1-49): ")
        if player_no in tab:
            print("Podales juz ta liczbe")
        else:
            tab.append(player_no)
            n += 1
        tab.sort()
    print(f"Twoje numerki: {tab}")
    for i in range(5):
        if tab[i] in computer_no[:6]:
            score += 1
    print(f"Szczesliwe numerki: {computer_no[:6]}")
    return f"Trafiles {score} raz/y"


print(lotto())
