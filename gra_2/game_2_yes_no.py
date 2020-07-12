def player():
    player = None
    while player != "tak" and player != "nie":
        player = input("Czy zgadlem?").lower()
        if player not in ("tak", "nie"):
            print("Mozliwe odpowiedzi to 'tak' lub 'nie'")
        else:
            return player


def guess_y_n():
    min = 0
    max = 1000
    input("Czy pomyslales juz liczbe?")
    for i in range(10):
        guess = int((max - min)/2 + min)
        print(f"Zgaduje: {guess}")
        player_answer = player()
        if player_answer == "tak":
            return f"--------------\nWygralem!\nTwoje liczba to: {guess}"
        elif player_answer == "nie":
            player_answer = input("Za duzo?")
            if player_answer == "tak":
                max = guess
            elif player_answer == "nie":
                player_answer = input("za malo?")
                if player_answer == "tak":
                    min = guess
                elif player_answer == "nie":
                    print("Nie oszukuj")
                    continue


print("""
Pomysl liczbe od 0 do 1000 a ja zgadne w 10 probach.
mozesz odpowiadac tylko 'za duzo', 'za malo', 'zgadles'
""")
print(guess_y_n())