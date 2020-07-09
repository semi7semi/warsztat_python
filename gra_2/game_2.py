def player():
    choices = ["za duzo", "za malo", "zgadles"]
    player = None
    while player not in choices:
        player = input("Czy zgadlem? ").lower()
        if player not in choices:
            print("Mozliwe odpowiedi to: 'za duzo, 'za malo, 'wygrales'")
        else:
            return player


def guess1000():
    min = 0
    max = 1000
    input("Czy pomyslales juz liczbe?")
    for i in range(10):
        guess = int((max - min)/2 + min)
        print(f"Zgaduje: {guess}")
        player_answer = player()
        if player_answer == "zgadles":
            return f"Wygralem! Twoje liczba to: {guess}"
        elif player_answer == "za duzo":
            max = guess
        elif player_answer == "za malo":
            min = guess
    return "Oszukujesz!"


print("""
Pomysl liczbe od 0 do 1000 a ja zgadne w 10 probach.
mozesz odpowiadac tylko 'za duzo', 'za malo', 'zgadles'
""")
print(guess1000())