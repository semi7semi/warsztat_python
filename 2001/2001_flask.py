import random
from flask import Flask, request, render_template


app = Flask(__name__)


def multi(score):
    """funkcja modyfikuje wynik przy rzucie 7 i 11"""
    roll = roll_dice()
    if roll == 7:
        return score // 7
    elif roll == 11:
        return score * 11
    else:
        return score + roll


def roll_dice():
    """symulacja rzutu koscmi oraz zsumowanie wyniku"""
    result = []
    for _ in range(2):
        dice_value = random.randint(1, 6)
        result.append(dice_value)
    return sum(result)


@app.route("/", methods=["GET", "POST"])
def game():
    if request.method == "GET":
        return render_template("index.html")
    else:
        player = int(request.form.get("player"))
        computer = int(request.form.get("computer"))
        player += roll_dice()
        computer += roll_dice()
        while player < 2001 and computer < 2001:
            player = multi(player)
            computer = multi(computer)
            return render_template("game.html", player=player, computer=computer)
        if player > computer:
            return "Wygrales!!!"
        else:
            return "Przegrales!"


if __name__ == "__main__":
    app.run(debug=True)
