import random
from flask import Flask, request, render_template


app = Flask(__name__)


def multi(score, x):
    """funkcja modyfikuje wynik przy rzucie 7 i 11"""
    roll = roll_dice(x)
    if roll == 7:
        return score // 7
    elif roll == 11:
        return score * 11
    else:
        return score + roll


def roll_dice(x):
    """symulacja rzutu koscmi oraz zsumowanie wyniku"""
    result = []
    for _ in range(x):
        dice_value = random.randint(1, 6)
        result.append(dice_value)
    print(result)
    return sum(result)


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


def choices(user_choice):
    """wybor ilosci kosci dla gracza"""
    if user_choice == "1 Dice":
        return 1
    elif user_choice == "2 Dices":
        return 2
    elif user_choice == "3 Dices":
        return 3
    else:
        return 4


@app.route("/", methods=["GET", "POST"])
def game():
    """Główna funkcja. zlicza kolejne rzuty az
    gracz lub komputer nie osiagna wymaganej wartosci.
    Oglasza zwyciezce"""
    if request.method == "GET":
        return render_template("index2.html")
    else:
        player = int(request.form.get("player"))
        computer = int(request.form.get("computer"))
        user_choice = request.form.get("user_choice")
        while player < 2001 and computer < 2001:
            player = multi(player, choices(user_choice))
            computer = multi_computer(computer)
            return render_template("game2.html", player=player, computer=computer)
        if player > computer:
            return f"""Wygrales!!! \nTwoj wynik {player}\nKomputrer {computer}"""
        else:
            return f"""Przegrales! \nTwoj wynik {player}\nKomputrer {computer} """


if __name__ == "__main__":
    app.run(debug=True)
