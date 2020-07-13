
def ask_yes_no(question):
    """zadaje pytanie i oczekuje na odpiwedz 'y' lub 'n'"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def guess_y_n():
    """glowna funkcja, zgaduje liczbe 10 razy"""
    min = 0
    max = 1000
    n = 0
    input("Czy pomyslales juz liczbe?")
    for i in range(10):
        guess = int((max - min)/2 + min)
        print(f"Zgaduje: {guess}")
        player_answer = ask_yes_no("Czy zgadlem? (y/n) ")
        if player_answer == "y":
            return f"--------------\nWygralem w {n} probach!\nTwoje liczba to: {guess}"
        elif player_answer == "n":
            player_answer = ask_yes_no("Czy za duzo? (y/n) ")
            if player_answer == "y":
                max = guess
                n += 1
            elif player_answer == "n":
                player_answer = ask_yes_no("czy za malo? (y/n) ")
                if player_answer == "y":
                    min = guess
                    n += 1
                elif player_answer == "n":
                    print("Nie oszukuj")
                    continue


print("""
Pomysl liczbe od 0 do 1000 a ja zgadne w 10 probach.
mozesz odpowiadac tylko tak lub nie (y / n)
""")
print(guess_y_n())