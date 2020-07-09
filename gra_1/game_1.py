import random


def guess_number(player_no=0):
    computer_no = random.randint(1, 100)
    guess = 0
    while player_no != computer_no:
        try:
            player_no = int(input("\nPodaj liczbe: "))
            guess += 1
            if player_no > computer_no:
                print("Za duzo!")
            elif player_no < computer_no:
                print("Za mało")
            else:
                return f"Wygrales!!! w {guess} probach."
        except ValueError:
            print("\npodaj Liczbe!")

print("""
Witaj w grze! 
Spróbuj odgadnąć o jakiej liczbe pomyslalem od 1 do 100
""")
print(guess_number())